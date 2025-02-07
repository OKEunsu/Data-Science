def visual_dim(dataframe, method : str, categorical_features : list , binary_features : list, continuous_features : list):
    import pandas as pd
    import numpy as np
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE
    import umap
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler

    # 레이블 데이터가 존재하는 경우, 라벨만 추출
    labels = dataframe['label'] if 'label' in dataframe.columns else None

    # 'label' 컬럼이 존재하면 삭제하고, 그렇지 않으면 그냥 dataframe 사용
    df_features = dataframe.drop(columns=['label'], errors='ignore')

    # 범주형과 연속형 변수 구분
    categorical_features = categorical_features
    binary_features = binary_features
    continuous_features = continuous_features
    

    # ColumnTransformer 설정
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), categorical_features),  
            ('bin', 'passthrough', binary_features),  # 그대로 유지
            ('scaled_num', StandardScaler(), continuous_features)
        ]
    )
# 변환
    processed_data = preprocessor.fit_transform(df_features)


    # 차원 축소 방법에 따른 처리
    if method == "PCA":
        pca = PCA(n_components=3)
        reduced_data = pca.fit_transform(processed_data)
        explained_variance = pca.explained_variance_ratio_
        print(f"PCA Explained Variance: {explained_variance}")

    elif method == "t-SNE":
        tsne = TSNE(n_components=3, random_state=42, perplexity=30, n_iter=1000)
        reduced_data = tsne.fit_transform(processed_data)

    elif method == "UMAP":
        reducer = umap.UMAP(n_components=3, random_state=42)  # 수정된 부분
        reduced_data = reducer.fit_transform(processed_data)

    else:
        raise ValueError("Invalid method. Choose 'PCA', 't-SNE', or 'UMAP'.")

    # 3D 시각화
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    if labels is not None:
        # 레이블이 있을 경우 색상별로 구분
        scatter = ax.scatter(
            reduced_data[:, 0], 
            reduced_data[:, 1], 
            reduced_data[:, 2], 
            c=labels,  # 라벨에 따라 색상 변경
            cmap='viridis',  # 색상 맵 설정
            alpha=0.6,
            edgecolors='w',
            s=50
        )
        # 범례 추가
        legend1 = ax.legend(*scatter.legend_elements(), title="Labels")
        ax.add_artist(legend1)
    else:
        # 레이블이 없을 경우 기본 색상으로 표시
        ax.scatter(
            reduced_data[:, 0], 
            reduced_data[:, 1], 
            reduced_data[:, 2], 
            c='blue', 
            alpha=0.6,
            edgecolors='w',
            s=50
        )

    ax.set_title(f"3D Visualization using {method}", fontsize=15)
    ax.set_xlabel("Component 1", fontsize=12)
    ax.set_ylabel("Component 2", fontsize=12)
    ax.set_zlabel("Component 3", fontsize=12)

    # 색상 바 (컬러 맵) 추가
    if labels is not None:
        plt.colorbar(scatter, ax=ax, label="Label")

    plt.show()