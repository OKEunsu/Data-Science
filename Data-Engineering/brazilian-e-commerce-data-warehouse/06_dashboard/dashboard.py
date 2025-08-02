# 📦 기본 라이브러리
import os
import io
import base64
from datetime import datetime

# 📄 환경 변수 로딩
from dotenv import load_dotenv

# 🐘 데이터베이스 연결
from sqlalchemy import create_engine

# 🐼 데이터 처리
import pandas as pd
import numpy as np

# 📊 시각화
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 📋 Streamlit
import streamlit as st

# 📄 PDF 리포트 (ReportLab)
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib import colors
from reportlab.lib.units import inch

# 🖋️ 한글 폰트 등록 (예: Nanum Gothic)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


@st.cache_data
def load_data():
    # env 파일 불러오기
    load_dotenv()

    # 환경설정
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    # 데이터 불러오기
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/olist_dm")

    # 테이블 직접 불러오기 (모든 컬럼)
    df_sales = pd.read_sql_table("fact_sales", con=engine)
    df_product = pd.read_sql_table("dim_product", con=engine)
    df_seller = pd.read_sql_table("dim_seller", con=engine)
    df_order_status = pd.read_sql_table("dim_order_status", con=engine)
    df_date = pd.read_sql_table("dim_date", con=engine)
    df_customer_orders = pd.read_sql_table("fact_customer_orders", con=engine)
    df_customer = pd.read_sql_table('dim_customer', con=engine)
    df_geolocation = pd.read_sql_table('dim_geolocation', con=engine)
    
    # 데이터 불러오기
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/olist")

    # 테이블 직접 불러오기 (모든 컬럼)
    df_order = pd.read_sql_table("orders", con=engine)
    df_order = df_order[['order_id', 'customer_id', 'order_approved_at', 'order_delivered_carrier_date',
        'order_delivered_customer_date', 'order_estimated_delivery_date']]
    
    df_customer_full = df_customer.merge(
    df_geolocation,
    left_on=['customer_zip_code_prefix', 'geolocation_city', 'geolocation_state'],
    right_on=['geolocation_zip_code_prefix', 'geolocation_city', 'geolocation_state'],
    how='left')

    df_customer_full = df_customer_full[['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'geolocation_city', 'geolocation_state', 'avg_lat', 'avg_lng']]
    df_customer_full.columns = ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state', 'customer_lat', 'customer_lng']
    df_seller.columns = ['seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state', 'seller_lat', 'seller_lng']

    df = df_sales.merge(df_product, how='left', on='product_id')
    df = df.merge(df_order_status, how='left', on='order_status')
    df = df.merge(df_seller, how='left', on='seller_id')
    df = df.merge(df_customer_orders, how='left', on=['order_id', 'order_date'])
    df = df.merge(df_customer_full, how='left', on='customer_id')
    df = df.merge(df_order, how='left', on=['order_id','customer_id'])

    df = df[[
        'order_id', 'order_item_id', 'product_id', 'seller_id', 'price',
        'freight_value', 'order_status', 'order_date',
        'order_approved_at', 'order_delivered_carrier_date',
        'order_delivered_customer_date', 'order_estimated_delivery_date',
        'product_category_name', 'product_category_name_english',
        'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm',
        'status_group',  # 주문 상태 그룹
        'seller_zip_code_prefix', 'seller_city', 'seller_state', 'seller_lat', 'seller_lng',
        'customer_id', 'customer_unique_id', 'customer_zip_code_prefix',
        'customer_city', 'customer_state', 'customer_lat', 'customer_lng',
        'payment_value', 'review_score'
    ]]
    
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['y_mth'] = df['order_date'].dt.strftime('%Y-%m')
    
    # 다른 날짜 컬럼들도 datetime 형식으로 변환
    date_columns = ['order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
        
    df = df[(df['order_date'] >= '2017-01') & (df['order_date'] <= '2018-08')]

    return df, df_geolocation

def apply_filters(df, selected_month, selected_state):
    """
    데이터프레임에 연월 및 지역 필터를 적용하는 함수
    
    Parameters:
    - df: 메인 데이터프레임
    - selected_month: 선택된 연월 ('All' 또는 'YYYY-MM' 형식)
    - selected_state: 선택된 지역 리스트 (빈 리스트면 전체 지역)
    
    Returns:
    - filtered_df: 필터링된 데이터프레임
    """
    filtered_df = df.copy()

    # 필터링 조건 적용
    # 1. 연월 필터: 'All'이 아닌 경우에만 필터링
    if selected_month != 'All':
        filtered_df = filtered_df[filtered_df['y_mth'] == selected_month]

    # 2. 지역 필터: 선택된 지역이 있는 경우에만 필터링 (빈 리스트일 때는 전체)
    if selected_state:  # 빈 리스트는 False, 값이 있으면 True
        filtered_df = filtered_df[filtered_df['customer_state'].isin(selected_state)]
    
    return filtered_df

def format_number(num):
    """
    숫자를 K, M 단위로 포맷팅하는 함수
    """
    if num >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num/1_000:.1f}K"
    else:
        return f"{num:,.0f}"

def calculate_metrics_with_comparison(filtered_df, selected_month, df, selected_state=[]):
    """
    현재 메트릭과 전월 대비 증감률을 계산하는 함수 (추가 메트릭 포함)
    """
    # ========================
    # 현재 메트릭 계산
    # ========================
    
    # 기존 메트릭
    current_total_amount = filtered_df.groupby('y_mth')['payment_value'].sum().sum() if not filtered_df.empty else 0
    current_total_orders = len(filtered_df['order_id'].unique()) if not filtered_df.empty else 0
    current_total_customers = len(filtered_df['customer_unique_id'].unique()) if not filtered_df.empty else 0
    current_avg_order_value = current_total_amount / current_total_orders if current_total_orders > 0 else 0
    current_total_products = len(filtered_df['product_id'].unique()) if not filtered_df.empty else 0
    
    # 추가 메트릭 계산
    current_on_time_delivery_rate = 0
    current_avg_shipping_time = 0
    current_repeat_purchase_rate = 0
    current_avg_review_score = 0
    
    if not filtered_df.empty:
        # 정시 배송률 (%)
        filtered_df_copy = filtered_df.copy()
        filtered_df_copy['on_time'] = filtered_df_copy['order_delivered_customer_date'] <= filtered_df_copy['order_estimated_delivery_date']
        current_on_time_delivery_rate = filtered_df_copy['on_time'].mean() * 100
        
        # 평균 배송 소요시간 (일수)
        filtered_df_copy['shipping_days'] = (filtered_df_copy['order_delivered_customer_date'] - filtered_df_copy['order_date']).dt.days
        current_avg_shipping_time = filtered_df_copy['shipping_days'].mean()
        
        # 재구매율
        customer_order_counts = filtered_df_copy.groupby('customer_unique_id')['order_id'].nunique()
        repeat_customers = (customer_order_counts >= 2).sum()
        total_customers = len(customer_order_counts)
        current_repeat_purchase_rate = (repeat_customers / total_customers) * 100 if total_customers > 0 else 0
        
        # 고객 평균 평점
        current_avg_review_score = filtered_df_copy.groupby('customer_id')['review_score'].mean().mean()
    
    # ========================
    # 전월 대비 계산
    # ========================
    can_compare = False
    prev_metrics = {}
    
    if selected_month != 'All':
        try:
            # 현재 월을 datetime으로 변환
            current_date = pd.to_datetime(selected_month, format='%Y-%m')
            # 전월 계산
            prev_date = current_date - pd.DateOffset(months=1)
            prev_month = prev_date.strftime('%Y-%m')
            
            # 전월 데이터가 있는지 확인
            if prev_month in df['y_mth'].values:
                # 전월 데이터 필터링 (지역 필터 적용)
                prev_df = df[df['y_mth'] == prev_month].copy()
                if selected_state:  # 지역 필터가 있으면 적용
                    prev_df = prev_df[prev_df['customer_state'].isin(selected_state)]
                
                if not prev_df.empty:
                    # 기존 메트릭
                    prev_total_amount = prev_df['payment_value'].sum()
                    prev_total_orders = len(prev_df['order_id'].unique())
                    prev_total_customers = len(prev_df['customer_unique_id'].unique())
                    prev_avg_order_value = prev_total_amount / prev_total_orders if prev_total_orders > 0 else 0
                    prev_total_products = len(prev_df['product_id'].unique())
                    
                    # 추가 메트릭
                    # 정시 배송률
                    prev_df['on_time'] = prev_df['order_delivered_customer_date'] <= prev_df['order_estimated_delivery_date']
                    prev_on_time_delivery_rate = prev_df['on_time'].mean() * 100
                    
                    # 평균 배송 소요시간
                    prev_df['shipping_days'] = (prev_df['order_delivered_customer_date'] - prev_df['order_date']).dt.days
                    prev_avg_shipping_time = prev_df['shipping_days'].mean()
                    
                    # 재구매율 (전월 기준)
                    prev_customer_order_counts = prev_df.groupby('customer_unique_id')['order_id'].nunique()
                    prev_repeat_customers = (prev_customer_order_counts >= 2).sum()
                    prev_total_customers_repeat = len(prev_customer_order_counts)
                    prev_repeat_purchase_rate = (prev_repeat_customers / prev_total_customers_repeat) * 100 if prev_total_customers_repeat > 0 else 0
                    
                    # 고객 평균 평점
                    prev_avg_review_score = prev_df.groupby('customer_id')['review_score'].mean().mean()
                    
                    prev_metrics = {
                        'total_amount': prev_total_amount,
                        'total_orders': prev_total_orders,
                        'total_customers': prev_total_customers,
                        'avg_order_value': prev_avg_order_value,
                        'total_products': prev_total_products,
                        'on_time_delivery_rate': prev_on_time_delivery_rate,
                        'avg_shipping_time': prev_avg_shipping_time,
                        'repeat_purchase_rate': prev_repeat_purchase_rate,
                        'avg_review_score': prev_avg_review_score
                    }
                    can_compare = True
        except Exception as e:
            print(f"전월 비교 계산 중 오류: {e}")
            can_compare = False
    
    current_metrics = {
        'total_amount': current_total_amount,
        'total_orders': current_total_orders,
        'total_customers': current_total_customers,
        'avg_order_value': current_avg_order_value,
        'total_products': current_total_products,
        'on_time_delivery_rate': current_on_time_delivery_rate,
        'avg_shipping_time': current_avg_shipping_time,
        'repeat_purchase_rate': current_repeat_purchase_rate,
        'avg_review_score': current_avg_review_score
    }

    return current_metrics, prev_metrics, can_compare

def calculate_delta(current, previous):
    """증감률 계산"""
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100

def create_regional_performance_section(df, filtered_df):
    """지역별 성과 분석을 위한 종합 시각화"""
    
    # ========================
    # 1. 메인 맵: 주별 매출 성과 (크기 + 색상) - 필터된 데이터 사용
    # ========================
    def create_main_performance_map(filtered_df):
        # 주별 성과 데이터 집계
        state_performance = filtered_df.groupby(['customer_state']).agg({
            'payment_value': ['sum', 'mean'],
            'order_id': 'nunique',
            'customer_unique_id': 'nunique',
            'review_score': 'mean',
            'customer_lat': 'mean',  # 대표 위치
            'customer_lng': 'mean'
        }).round(2)
        
        # 컬럼명 정리
        state_performance.columns = ['total_sales', 'avg_order_value', 'total_orders', 'total_customers', 'avg_rating', 'lat', 'lng']
        state_performance = state_performance.reset_index()
        
        # 성과 점수 계산 (매출 + 평점 + 주문수를 종합)
        state_performance['performance_score'] = (
            (state_performance['total_sales'] / state_performance['total_sales'].max() * 0.4) +
            (state_performance['avg_rating'] / 5 * 0.3) +
            (state_performance['total_orders'] / state_performance['total_orders'].max() * 0.3)
        ) * 100
        
        fig = px.scatter_mapbox(
            state_performance,
            lat='lat',
            lon='lng',
            size='total_sales',
            color='performance_score',
            hover_name='customer_state',
            hover_data={
                'total_sales': ':,.0f',
                'total_orders': ':,',
                'total_customers': ':,',
                'avg_order_value': ':,.0f',
                'avg_rating': ':.1f',
                'performance_score': ':.1f'
            },
            color_continuous_scale='RdYlGn',  # 빨강(낮음) → 노랑 → 초록(높음)
            size_max=30,
            zoom=2,
            center=dict(lat=-14.2350, lon=-51.9253),
            title='🎯 주별 종합 성과 지표 (필터 적용)'
        )
        
        fig.update_layout(
            mapbox_style='open-street-map',
            height=600,
            coloraxis_colorbar=dict(
                title="성과 점수",
                ticksuffix="점"
            )
        )
        
        return fig
    
    # ========================
    # 2. 핵심 KPI 카드들 - 필터된 데이터 사용
    # ========================
    def get_key_metrics(filtered_df):
        """핵심 지표 계산 - 필터된 데이터 기준"""
        total_sales = filtered_df['payment_value'].sum()
        total_orders = filtered_df['order_id'].nunique()
        total_customers = filtered_df['customer_unique_id'].nunique()
        avg_rating = filtered_df['review_score'].mean()
        total_states = filtered_df['customer_state'].nunique()
        
        # 재구매율 계산
        customer_orders = filtered_df.groupby('customer_unique_id')['order_id'].nunique()
        repeat_rate = ((customer_orders >= 2).sum() / len(customer_orders)) * 100 if len(customer_orders) > 0 else 0
        
        return {
            'total_sales': total_sales,
            'total_orders': total_orders,
            'total_customers': total_customers,
            'avg_rating': avg_rating,
            'total_states': total_states,
            'repeat_rate': repeat_rate
        }
    
    # ========================
    # 3. 상위/하위 성과 지역 랭킹 - 필터된 데이터 사용
    # ========================
    def create_top_bottom_ranking(filtered_df):
        # 주별 데이터 준비
        state_data = filtered_df.groupby('customer_state').agg({
            'payment_value': 'sum',
            'order_id': 'nunique',
            'customer_unique_id': 'nunique',
            'review_score': 'mean'
        }).reset_index()
        
        state_data.columns = ['state', 'total_sales', 'total_orders', 'total_customers', 'avg_rating']
        
        # 상위 8개, 하위 5개 주 선택
        top_states = state_data.nlargest(8, 'total_sales')
        bottom_states = state_data.nsmallest(5, 'total_sales')
        
        return top_states, bottom_states
    
    # ========================
    # 4. 지역별 성과 메트릭 테이블 - 필터된 데이터 사용
    # ========================
    def create_performance_summary(filtered_df):
        # 주별 상세 성과 데이터
        state_details = filtered_df.groupby('customer_state').agg({
            'payment_value': 'sum',
            'review_score': 'mean',
            'order_id': 'nunique'
        }).round(2)
        
        state_details.columns = ['매출', '평점', '주문수']
        state_details = state_details.reset_index()
        state_details = state_details.sort_values('매출', ascending=False)
        
        return state_details
    
    # ========================
    # 5. 월별 상위 지역 트렌드 - 전체 데이터 사용 (트렌드는 전체적인 패턴을 봐야 함)
    # ========================
    def create_top_states_trend(df):
        # 전체 데이터에서 상위 5개 주의 월별 트렌드
        top_states = df.groupby('customer_state')['payment_value'].sum().nlargest(5).index
        
        trend_data = df[df['customer_state'].isin(top_states)].groupby(['y_mth', 'customer_state'])['payment_value'].sum().reset_index()
        
        fig = px.line(
            trend_data,
            x='y_mth',
            y='payment_value',
            color='customer_state',
            title='📈 상위 5개 주 매출 트렌드 (전체 기간)',
            markers=True
        )
        
        fig.update_layout(
            height=300,
            xaxis_title='월',
            yaxis_title='매출 (BRL)',
            legend_title='주',
            yaxis=dict(tickformat='~s'),
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="top",
                y=1,
                xanchor="left",
                x=1.02
            )
        )
        
        return fig
    
    # ========================
    # 6. 지역별 고객 만족도 vs 매출 산점도 - 전체 데이터 사용
    # ========================
    def create_satisfaction_vs_sales(df):
        # 전체 데이터로 전반적인 패턴 분석
        state_data = df.groupby('customer_state').agg({
            'payment_value': 'sum',
            'review_score': 'mean',
            'order_id': 'nunique'
        }).reset_index()
        
        fig = px.scatter(
            state_data,
            x='review_score',
            y='payment_value',
            size='order_id',
            hover_name='customer_state',
            title='⭐ 고객 만족도 vs 매출 관계 (전체 데이터)',
            labels={
                'review_score': '평균 평점',
                'payment_value': '총 매출 (BRL)',
                'order_id': '주문수'
            }
        )
        
        fig.update_layout(height=300)
        
        return fig
    
    # ========================
    # 7. 전체 vs 필터 비교 지표
    # ========================
    def get_comparison_metrics(df, filtered_df):
        """전체 데이터 대비 필터된 데이터 비교"""
        # 전체 데이터 지표
        total_all_sales = df['payment_value'].sum()
        total_all_orders = df['order_id'].nunique()
        total_all_customers = df['customer_unique_id'].nunique()
        
        # 필터된 데이터 지표
        total_filtered_sales = filtered_df['payment_value'].sum()
        total_filtered_orders = filtered_df['order_id'].nunique()
        total_filtered_customers = filtered_df['customer_unique_id'].nunique()
        
        # 비율 계산
        sales_ratio = (total_filtered_sales / total_all_sales) * 100 if total_all_sales > 0 else 0
        orders_ratio = (total_filtered_orders / total_all_orders) * 100 if total_all_orders > 0 else 0
        customers_ratio = (total_filtered_customers / total_all_customers) * 100 if total_all_customers > 0 else 0
        
        return {
            'sales_ratio': sales_ratio,
            'orders_ratio': orders_ratio,
            'customers_ratio': customers_ratio,
            'total_all_sales': total_all_sales,
            'total_filtered_sales': total_filtered_sales
        }
    
    return (create_main_performance_map, get_key_metrics, create_top_bottom_ranking, 
            create_performance_summary, create_top_states_trend, create_satisfaction_vs_sales,
            get_comparison_metrics)

# Streamlit 대시보드 구성
def display_regional_performance_dashboard(df, filtered_df):
    """지역별 성과 분석 대시보드 표시"""
    
    st.markdown("---")
    st.subheader("🌎 지역별 성과 분석")
    
    # 함수들 가져오기
    (create_main_map, get_key_metrics, create_top_bottom_ranking, 
     create_performance_summary, create_trend, create_scatter,
     get_comparison_metrics) = create_regional_performance_section(df, filtered_df)
    
    # ========================
    # 0행: 전체 vs 필터 비교 요약
    # ========================
    comparison_metrics = get_comparison_metrics(df, filtered_df)
    
    st.markdown("#### 📊 필터 적용 현황")
    col_comp1, col_comp2, col_comp3, col_comp4 = st.columns(4)
    
    with col_comp1:
        st.metric(
            "매출 비중", 
            f"{comparison_metrics['sales_ratio']:.1f}%",
            f"{comparison_metrics['total_filtered_sales']:,.0f} / {comparison_metrics['total_all_sales']:,.0f} BRL"
        )
    
    with col_comp2:
        st.metric(
            "주문 비중", 
            f"{comparison_metrics['orders_ratio']:.1f}%"
        )
    
    with col_comp3:
        st.metric(
            "고객 비중", 
            f"{comparison_metrics['customers_ratio']:.1f}%"
        )
    
    with col_comp4:
        # 필터가 얼마나 선택적인지 표시
        selectivity = 100 - comparison_metrics['sales_ratio']
        st.metric(
            "필터 선택도", 
            f"{selectivity:.1f}%",
            "제외된 데이터 비율"
        )
    
    st.markdown("---")
    
    # ========================
    # 1행: 메인 성과 맵 + 사이드바 정보
    # ========================
    col_map, col_sidebar = st.columns([2, 1])
    
    with col_map:
        fig_main = create_main_map(filtered_df)
        st.plotly_chart(fig_main, use_container_width=True)
    
    with col_sidebar:
        # 핵심 지표 카드들
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("#### 📊 핵심 지표 (필터 적용)")
        metrics = get_key_metrics(filtered_df)
        
        col_metric1, col_metric2 = st.columns(2)
        with col_metric1:
            st.metric("총 매출", f"{metrics['total_sales']:,.0f}")
            st.metric("총 고객수", f"{metrics['total_customers']:,}")
            st.metric("참여 주", f"{metrics['total_states']}")
        
        with col_metric2:
            st.metric("총 주문수", f"{metrics['total_orders']:,}")
            st.metric("평균 평점", f"{metrics['avg_rating']:.2f}/5")
            st.metric("재구매율", f"{metrics['repeat_rate']:.1f}%")
    
    # 성과 지표 설명
    with st.expander("📖 성과 점수 계산 방식"):
        st.write("""
        **종합 성과 점수 = 매출 비중(40%) + 평점 비중(30%) + 주문수 비중(30%)**
        - 🔴 낮은 성과 (0-40점)
        - 🟡 보통 성과 (40-70점)  
        - 🟢 높은 성과 (70-100점)
        
        원의 크기는 총 매출액을 반영합니다.
        
        ⚠️ **주의**: 지도와 랭킹은 필터된 데이터를 기준으로 합니다.
        """)

    top_states, bottom_states = create_top_bottom_ranking(filtered_df)
    
    rank_col1, rank_col2 = st.columns(2)
    with rank_col1:
        # 상위 지역 랭킹
        st.markdown("### 🏆 매출 상위 지역 (필터 기준)")
        # 상위 5개만 표시 (공간 절약)
        for i, row in top_states.head(5).iterrows():
            with st.container():
                st.markdown(f"""
                <div style="background: linear-gradient(90deg, #2E8B57 0%, #90EE90 100%); 
                            padding: 8px; margin: 4px 0; border-radius: 5px; color: white;">
                    <strong>{row['state']}</strong><br>
                    💰 {row['total_sales']:,.0f} BRL<br>
                    📦 {row['total_orders']:,} 주문
                </div>
                """, unsafe_allow_html=True)
    
    with rank_col2:
        # 개선 필요 지역
        st.markdown("### 📈 개선 기회 지역 (필터 기준)")
        for i, row in bottom_states.head(3).iterrows():
            with st.container():
                st.markdown(f"""
                <div style="background: linear-gradient(90deg, #CD5C5C 0%, #FFA07A 100%); 
                            padding: 8px; margin: 4px 0; border-radius: 5px; color: white;">
                    <strong>{row['state']}</strong><br>
                    💰 {row['total_sales']:,.0f} BRL<br>
                    ⭐ {row['avg_rating']:.1f}/5
                </div>
                """, unsafe_allow_html=True)

    
    # ========================
    # 2행: 추가 분석 차트들
    # ========================
    col_trend, col_scatter = st.columns(2)
    
    with col_trend:
        fig_trend = create_trend(df)  # 전체 데이터로 트렌드 분석
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with col_scatter:
        fig_scatter = create_scatter(df)  # 전체 데이터로 패턴 분석
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # ========================
    # 3행: 전체 지역 성과 요약 테이블
    # ========================
    with st.expander("📋 전체 지역별 상세 성과 (필터 적용)"):
        performance_summary = create_performance_summary(filtered_df)
        
        # 테이블을 3개 컬럼으로 나누어 표시
        col_table1, col_table2, col_table3 = st.columns(3)
        
        rows_per_col = len(performance_summary) // 3 + 1
        
        with col_table1:
            st.dataframe(
                performance_summary.iloc[:rows_per_col].set_index('customer_state'),
                use_container_width=True
            )
        
        with col_table2:
            st.dataframe(
                performance_summary.iloc[rows_per_col:rows_per_col*2].set_index('customer_state'),
                use_container_width=True
            )
        
        with col_table3:
            st.dataframe(
                performance_summary.iloc[rows_per_col*2:].set_index('customer_state'),
                use_container_width=True
            )
    
    # ========================
    # 4행: 핵심 인사이트
    # ========================
    with st.expander("💡 핵심 인사이트 & 추천사항"):
        # 필터된 데이터로 인사이트 생성
        state_summary = filtered_df.groupby('customer_state').agg({
            'payment_value': 'sum',
            'review_score': 'mean',
            'order_id': 'nunique'
        })
        
        if len(state_summary) > 0:
            best_sales_state = state_summary['payment_value'].idxmax()
            best_rating_state = state_summary['review_score'].idxmax()
            most_orders_state = state_summary['order_id'].idxmax()
            
            col_insight1, col_insight2, col_insight3 = st.columns(3)
            
            with col_insight1:
                st.markdown("#### 🏆 성과 우수 지역")
                st.success(f"""
                **매출 1위**: {best_sales_state}  
                💰 {state_summary.loc[best_sales_state, 'payment_value']:,.0f} BRL
                
                **평점 1위**: {best_rating_state}  
                ⭐ {state_summary.loc[best_rating_state, 'review_score']:.2f}/5
                """)
            
            with col_insight2:
                st.markdown("#### 📊 시장 분석")
                total_sales = state_summary['payment_value'].sum()
                if len(state_summary) >= 3:
                    top_3_sales = state_summary['payment_value'].nlargest(3).sum()
                    concentration = (top_3_sales / total_sales) * 100
                else:
                    concentration = 100.0
                
                st.info(f"""
                **시장 집중도**: {concentration:.1f}%  
                (상위 3개 주가 전체 매출의 {concentration:.1f}% 차지)
                
                **활성 주문 지역**: {most_orders_state}  
                📦 {state_summary.loc[most_orders_state, 'order_id']:,} 주문
                """)
            
            with col_insight3:
                st.markdown("#### 🎯 개선 제안")
                # 개선 기회가 있는 지역 (매출 대비 평점이 낮은 곳)
                state_summary['efficiency'] = state_summary['review_score'] / (state_summary['payment_value'] / 1000)
                improvement_target = state_summary['efficiency'].idxmin()
                
                st.warning(f"""
                **집중 지원 필요**: {improvement_target}  
                매출 대비 고객만족도 개선 필요
                
                **확장 기회**: 하위 지역 마케팅 강화  
                신규 고객 유치 및 브랜드 인지도 제고
                """)
        else:
            st.warning("필터 조건에 해당하는 데이터가 없습니다.")

def create_pdf_report(df, filtered_df, selected_month, selected_state, current_metrics, prev_metrics, can_compare):
    """
    대시보드 데이터를 PDF 리포트로 생성하는 함수
    """
    # 폰트 등록
    pdfmetrics.registerFont(TTFont('NanumGothic', 'NanumGothic.ttf'))

    # PDF 버퍼 생성
    buffer = io.BytesIO()
    
    # PDF 문서 생성
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # 스타일 설정
    styles = getSampleStyleSheet()
    
    # 커스텀 스타일 추가
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName='NanumGothic',
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontName='NanumGothic',
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.darkblue
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontName='NanumGothic',
        fontSize=12,
        spaceAfter=6,
        spaceBefore=12,
        textColor=colors.blue
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontName='NanumGothic',
        fontSize=10,
        spaceAfter=6
    )
    
    # PDF 내용 구성
    story = []
    
    # 1. 제목 및 기본 정보
    story.append(Paragraph("Brazilian E-Commerce Dashboard Report", title_style))
    story.append(Spacer(1, 12))
    
    # 리포트 생성 정보
    report_info = f"""
    <b>리포트 생성일:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>
    <b>분석 기간:</b> {selected_month if selected_month != 'All' else '전체 기간'}<br/>
    <b>분석 지역:</b> {', '.join(selected_state) if selected_state else '전체 지역'}<br/>
    """
    story.append(Paragraph(report_info, normal_style))
    story.append(Spacer(1, 20))
    
    # 2. 핵심 KPI 요약
    story.append(Paragraph("📊 핵심 성과 지표", heading_style))
    
    # KPI 테이블 데이터 준비
    kpi_data = [
        ['지표', '현재 값', '전월 대비' if can_compare else '상태'],
        ['Total Amount', f"{current_metrics['total_amount']:,.0f} BRL", 
         f"{((current_metrics['total_amount'] - prev_metrics.get('total_amount', 0)) / prev_metrics.get('total_amount', 1) * 100):.1f}%" if can_compare and prev_metrics.get('total_amount', 0) > 0 else 'N/A'],
        ['Total Orders', f"{current_metrics['total_orders']:,}", 
         f"{((current_metrics['total_orders'] - prev_metrics.get('total_orders', 0)) / prev_metrics.get('total_orders', 1) * 100):.1f}%" if can_compare and prev_metrics.get('total_orders', 0) > 0 else 'N/A'],
        ['Total Customers', f"{current_metrics['total_customers']:,}", 
         f"{((current_metrics['total_customers'] - prev_metrics.get('total_customers', 0)) / prev_metrics.get('total_customers', 1) * 100):.1f}%" if can_compare and prev_metrics.get('total_customers', 0) > 0 else 'N/A'],
        ['Aov', f"{current_metrics['avg_order_value']:,.0f} BRL", 
         f"{((current_metrics['avg_order_value'] - prev_metrics.get('avg_order_value', 0)) / prev_metrics.get('avg_order_value', 1) * 100):.1f}%" if can_compare and prev_metrics.get('avg_order_value', 0) > 0 else 'N/A'],
        ['Total Products', f"{current_metrics['total_products']:,}", 
         f"{((current_metrics['total_products'] - prev_metrics.get('total_products', 0)) / prev_metrics.get('total_products', 1) * 100):.1f}%" if can_compare and prev_metrics.get('total_products', 0) > 0 else 'N/A']
    ]
    
    # KPI 테이블 생성
    kpi_table = Table(kpi_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
    kpi_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'NanumGothic'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(kpi_table)
    story.append(Spacer(1, 20))
    
    # 3. 운영 지표
    story.append(Paragraph("🚚 운영 성과 지표", heading_style))
    
    operational_data = [
        ['지표', '현재 값', '목표/기준'],
        ['On-time Delivery Rate', f"{current_metrics['on_time_delivery_rate']:.1f}%", f"95% or higher"],
        ['Average Shipping Time', f"{current_metrics['avg_shipping_time']:.1f}days", "Within 7 days"],
        ['Repeat Purchase Rate', f"{current_metrics['repeat_purchase_rate']:.2f}%", "Over 30%"],
        ['Average Review Score', f"{current_metrics['avg_review_score']:.2f}/5", "At least 4.0"]
    ]
    
    operational_table = Table(operational_data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
    operational_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'NanumGothic'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(operational_table)
    story.append(Spacer(1, 20))
    
    # 4. 상위 카테고리 분석
    story.append(Paragraph("📈 상위 제품 카테고리 분석", heading_style))
    
    # 상위 10개 카테고리 데이터
    top_categories = (
        filtered_df.groupby('product_category_name')['payment_value']
        .sum()
        .nlargest(10)
        .reset_index()
    )

    story.append(Spacer(1, 20))
                 
    category_data = [['순위', '카테고리', '매출 (BRL)', '비중 (%)']]
    total_sales = top_categories['payment_value'].sum()
    
    for idx, row in top_categories.iterrows():
        rank = idx + 1
        category = row['product_category_name'][:20] + "..." if len(row['product_category_name']) > 20 else row['product_category_name']
        sales = f"{row['payment_value']:,.0f}"
        percentage = f"{(row['payment_value'] / total_sales * 100):.1f}"
        category_data.append([str(rank), category, sales, percentage])
    
    category_table = Table(category_data, colWidths=[0.6*inch, 2.4*inch, 1.5*inch, 1*inch])
    category_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'NanumGothic'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(category_table)
    
    # 5. 지역별 성과 분석
    story.append(Paragraph("🌎 지역별 성과 분석", heading_style))
    
    # 지역별 데이터 준비
    regional_data = filtered_df.groupby('customer_state').agg({
        'payment_value': 'sum',
        'order_id': 'nunique',
        'customer_unique_id': 'nunique',
        'review_score': 'mean'
    }).round(2).reset_index()
    
    regional_data = regional_data.sort_values('payment_value', ascending=False).head(15)
    
    # 지역별 테이블
    regional_table_data = [['순위', '주', '매출 (BRL)', '주문수', '고객수', '평점']]
    
    for idx, row in regional_data.iterrows():
        rank = len(regional_table_data)
        state = row['customer_state']
        sales = f"{row['payment_value']:,.0f}"
        orders = f"{row['order_id']:,}"
        customers = f"{row['customer_unique_id']:,}"
        rating = f"{row['review_score']:.2f}"
        regional_table_data.append([str(rank), state, sales, orders, customers, rating])
    
    regional_table = Table(regional_table_data, colWidths=[0.5*inch, 0.8*inch, 1.3*inch, 1*inch, 1*inch, 0.8*inch])
    regional_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'NanumGothic'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(regional_table)
    story.append(Spacer(1, 20))
    
    # 6. 월별 트렌드 요약
    if selected_month == 'All':
        story.append(Paragraph("📊 월별 매출 트렌드", heading_style))
        
        monthly_data = df.groupby('y_mth')['payment_value'].sum().reset_index()
        
        # 월별 데이터를 테이블로 표시 (최근 12개월)
        monthly_table_data = [['월', '매출 (BRL)', '전월 대비']]
        
        for idx, row in monthly_data.tail(12).iterrows():
            month = row['y_mth']
            sales = f"{row['payment_value']:,.0f}"
            
            # 전월 대비 계산
            if idx > 0:
                prev_sales = monthly_data.iloc[idx-1]['payment_value']
                growth = ((row['payment_value'] - prev_sales) / prev_sales * 100) if prev_sales > 0 else 0
                growth_str = f"{growth:+.1f}%"
            else:
                growth_str = "N/A"
            
            monthly_table_data.append([month, sales, growth_str])
        
        monthly_table = Table(monthly_table_data, colWidths=[1.5*inch, 2*inch, 1.5*inch])
        monthly_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'NanumGothic'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(monthly_table)
        story.append(Spacer(1, 20))
    
    # 7. 주요 인사이트 및 권장사항
    story.append(Paragraph("💡 주요 인사이트 및 권장사항", heading_style))
    
    insights = []
    
    # 매출 인사이트
    if current_metrics['total_amount'] > 0:
        insights.append(f"• 현재 총 매출: {current_metrics['total_amount']:,.0f} BRL")
        insights.append(f"• 평균 주문 금액: {current_metrics['avg_order_value']:,.0f} BRL")
    
    # 운영 인사이트
    if current_metrics['on_time_delivery_rate'] < 90:
        insights.append("• ⚠️ 정시 배송률이 90% 미만입니다. 물류 프로세스 개선이 필요합니다.")
    
    if current_metrics['avg_review_score'] < 4.0:
        insights.append("• ⚠️ 고객 평점이 4.0 미만입니다. 고객 만족도 향상 방안을 검토해주세요.")
    
    if current_metrics['repeat_purchase_rate'] < 20:
        insights.append("• ⚠️ 재구매율이 낮습니다. 고객 유지 전략을 강화해주세요.")
    
    # 권장사항
    insights.append("\n📋 권장사항:")
    insights.append("• 상위 카테고리에 마케팅 집중 투자")
    insights.append("• 성과가 좋은 지역의 성공 요인을 다른 지역에 적용")
    insights.append("• 배송 시간 단축을 위한 물류 센터 최적화")
    insights.append("• 고객 만족도 향상을 위한 서비스 개선")
    
    for insight in insights:
        story.append(Paragraph(insight, normal_style))
    
    story.append(Spacer(1, 20))
    
    # 8. 푸터
    footer_text = f"""
    <br/><br/>
    <i>본 리포트는 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}에 생성되었습니다.</i><br/>
    <i>Brazilian E-Commerce Dashboard - Automated Report</i>
    """
    story.append(Paragraph(footer_text, normal_style))
    
    # PDF 생성
    doc.build(story)
    
    # 버퍼에서 PDF 데이터 가져오기
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data

# Streamlit에서 PDF 다운로드 버튼을 구현하는 함수
def generate_download_button(df, filtered_df, selected_month, selected_state, current_metrics, prev_metrics, can_compare):
    """
    Streamlit에서 사용할 PDF 다운로드 버튼 생성
    """
    try:
        # PDF 생성
        pdf_data = create_pdf_report(
            df, filtered_df, selected_month, selected_state, 
            current_metrics, prev_metrics, can_compare
        )
        
        # 파일명 생성
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        month_str = selected_month if selected_month != 'All' else 'all'
        state_str = '_'.join(selected_state[:2]) if selected_state else 'all'
        filename = f"dashboard_report_{month_str}_{state_str}_{timestamp}.pdf"
        
        return pdf_data, filename
        
    except Exception as e:
        st.error(f"PDF 생성 중 오류가 발생했습니다: {str(e)}")
        return None, None

# 기존 사이드바 PDF 다운로드 부분을 다음으로 교체:
def update_sidebar_download(df, filtered_df, selected_month, selected_state, current_metrics, prev_metrics, can_compare):
    """
    사이드바 PDF 다운로드 섹션 업데이트
    """
    st.sidebar.markdown("---")
    st.sidebar.subheader("📄 리포트 다운로드")
    
    # PDF 생성 및 다운로드 버튼
    if st.sidebar.button("📊 PDF 리포트 생성", use_container_width=True):
        with st.sidebar:
            with st.spinner('PDF 리포트를 생성하고 있습니다...'):
                pdf_data, filename = generate_download_button(
                    df, filtered_df, selected_month, selected_state,
                    current_metrics, prev_metrics, can_compare
                )
                
                if pdf_data and filename:
                    st.sidebar.download_button(
                        label="📥 PDF 다운로드",
                        data=pdf_data,
                        file_name=filename,
                        mime="application/pdf",
                        use_container_width=True
                    )
                    st.sidebar.success("PDF 리포트가 생성되었습니다!")
                else:
                    st.sidebar.error("PDF 생성에 실패했습니다.")
    
    # 리포트 정보 표시
    with st.sidebar.expander("📋 리포트 내용"):
        st.write("""
        **포함 내용:**
        - 📊 핵심 성과 지표 요약
        - 🚚 운영 성과 지표
        - 📈 상위 제품 카테고리 분석
        - 🌎 지역별 성과 분석
        - 📊 월별 트렌드 (전체 기간 선택시)
        - 💡 인사이트 및 권장사항
        
        **특징:**
        - 현재 필터 조건 반영
        - 전월 대비 증감률 포함
        - 표와 차트로 시각화
        - 자동 생성된 인사이트
        """)

# --------------
# 대시보드 TITLE
# --------------
st.set_page_config(page_title="Brazilian E-Commerce Dashboard", layout="wide")
st.title("Brazilian E-Commerce 대시보드")

# --------------
# LOAD DATA
# --------------
df, df_geolocation = load_data()

# --------------
# SIDE BAR
# --------------
# STATE 옵션

st.markdown(
    """
    <style>
        /* 사이드바 컨테이너의 너비를 고정 */
        [data-testid="stSidebar"] {
            max-width: 400px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

state_options = df_geolocation['geolocation_state'].unique().tolist()

# 연월 옵션
year_mth_list = ['All'] + sorted(df['y_mth'].unique())

st.sidebar.title("필터 옵션")
selected_month = st.sidebar.selectbox("연월 선택", year_mth_list, index=0)
selected_state = st.sidebar.multiselect("지역 선택", state_options)

# 필터링
filtered_df = apply_filters(df, selected_month, selected_state)


# -------------
# 상단 KPI
# -------------

# 메트릭 계산
current_metrics, prev_metrics, can_compare = calculate_metrics_with_comparison(
    filtered_df, selected_month, df, selected_state
)

# 증감률 계산 (비교 가능한 경우만)
deltas = {}
if can_compare:
    for key in current_metrics.keys():
        delta_pct = calculate_delta(current_metrics[key], prev_metrics[key])
        deltas[key] = delta_pct

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "총 매출", 
    f"{format_number(current_metrics['total_amount'])} BRL",
    delta=f"{deltas.get('total_amount', 0):.1f}%" if can_compare and deltas.get('total_amount') is not None else None
)

col2.metric(
    "총 주문 수", 
    f"{format_number(current_metrics['total_orders'])}",
    delta=f"{deltas.get('total_orders', 0):.1f}%" if can_compare and deltas.get('total_orders') is not None else None
)

col3.metric(
    "고객 수", 
    f"{format_number(current_metrics['total_customers'])}",
    delta=f"{deltas.get('total_customers', 0):.1f}%" if can_compare and deltas.get('total_customers') is not None else None
)

col4.metric(
    "평균 주문 금액", 
    f"{current_metrics['avg_order_value']:,.0f} BRL",
    delta=f"{deltas.get('avg_order_value', 0):.1f}%" if can_compare and deltas.get('avg_order_value') is not None else None
)

col5.metric(
    "상품 수", 
    f"{format_number(current_metrics['total_products'])}",
    delta=f"{deltas.get('total_products', 0):.1f}%" if can_compare and deltas.get('total_products') is not None else None
)

# --------------
# 경영지표 시각화
# --------------

# 공백
st.markdown("<br>", unsafe_allow_html=True) # HTML의 <br> 태그 사용

# UI 표시
chart1, chart2 = st.columns(2)

# 데이터 준비
monthly_data = df.groupby('y_mth')['payment_value'].sum().reset_index()

# --------------
# 월별 매출
# --------------
fig = px.line(
    monthly_data,
    x='y_mth',
    y='payment_value',
    title='월별 결제 금액',
    markers=True
)

# 축 설정
fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    yaxis=dict(tickformat='~s')
)

# 선택된 월 하이라이트 (add_shape 사용)
if selected_month != 'All' and selected_month in monthly_data['y_mth'].values:
    fig.add_shape(
        type="line",
        x0=selected_month, x1=selected_month,
        y0=0, y1=1,
        yref="paper",  # y축을 전체 차트 높이 기준으로
        line=dict(color="red", width=2, dash="dash")
    )
    
    # 텍스트 주석 추가
    fig.add_annotation(
        x=selected_month,
        y=monthly_data[monthly_data['y_mth'] == selected_month]['payment_value'].iloc[0],
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
    )

chart1.plotly_chart(fig, use_container_width=True)

# ------------------------
# 상위 5개 카테고리별 매출
# ------------------------

top5_categories = (
    filtered_df.groupby('product_category_name')['payment_value']
    .sum()
    .nlargest(5)  # 상위 5개만
).reset_index()

# 결과 조
top5_categories.columns = ['product_category_name', 'sum_amount']
top5_categories = top5_categories.sort_values('sum_amount', ascending=True)

fig = px.bar(
    top5_categories, 
    x='sum_amount', 
    y='product_category_name',
    orientation='h',  # 수평 바차트
    title=f'[{selected_month}] 상위 5개 카테고리별 매출'
)

fig.update_layout(
    xaxis_title=None,
    yaxis_title=None,
    yaxis=dict(tickformat='~s')
)

chart2.plotly_chart(fig, use_container_width=True)

# 공백
st.markdown("<br>", unsafe_allow_html=True) # HTML의 <br> 태그 사용

# --------------
# 중단 KPI 카드
# --------------

# UI 표시
m_col1, m_col2, m_col3, m_col4,  = st.columns(4)

# 정시 배송률(%)
filtered_df['on_time'] = filtered_df['order_delivered_customer_date'] <= filtered_df['order_estimated_delivery_date']
on_time_delivery_rate = filtered_df['on_time'].mean() * 100

# 평균 배송 소요시간 (일수)
filtered_df['shipping_days'] = (filtered_df['order_delivered_customer_date'] - filtered_df['order_date']).dt.days
avg_shipping_time = filtered_df['shipping_days'].mean()

# 재구매율
# 고객별 주문 횟수
customer_order_counts = filtered_df.groupby('customer_unique_id')['order_id'].nunique()
# 2회 이상 주문한 고객 수
repeat_customers = (customer_order_counts >= 2).sum()
# 전체 고객 수
total_customers = len(customer_order_counts)
# 재구매율
repeat_purchase_rate = (repeat_customers / total_customers) * 100

# 고객 평균 평점
avg_review_score = filtered_df.groupby('customer_id')['review_score'].mean().mean()

m_col1.metric(
    "정시 배송률", 
    f"{current_metrics['on_time_delivery_rate']:.1f}%",
    delta=f"{deltas.get('on_time_delivery_rate', 0):.1f}%" if can_compare and deltas.get('on_time_delivery_rate') is not None else None,
)

m_col2.metric(
    "평균 배송 소요시간", 
    f"{current_metrics['avg_shipping_time']:.1f}일",
    delta=f"{deltas.get('avg_shipping_time', 0):.1f}%" if can_compare and deltas.get('avg_shipping_time') is not None else None,
    delta_color = 'inverse'
)

m_col3.metric(
    "재구매율", 
    f"{current_metrics['repeat_purchase_rate']:.2f}%",
    delta=f"{deltas.get('repeat_purchase_rate', 0):.2f}%" if can_compare and deltas.get('repeat_purchase_rate') is not None else None
)

m_col4.metric(
    "고객 평균 평점", 
    f"{current_metrics['avg_review_score']:.2f}/5",
    delta=f"{deltas.get('avg_review_score', 0):.2f}%" if can_compare and deltas.get('avg_review_score') is not None else None
)

# --------------
# 지역별 성과
# --------------
display_regional_performance_dashboard(df, filtered_df)

# 사이드바 다운로드 부분
update_sidebar_download(
    df,
    filtered_df,
    selected_month,
    selected_state,
    current_metrics,
    prev_metrics,
    can_compare

)
