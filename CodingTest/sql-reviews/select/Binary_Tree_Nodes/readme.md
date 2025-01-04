# 문제 : Binary Tree Nodes
### [Binary Tree Nodes]([https://school.programmers.co.kr/learn/courses/30/lessons/151141](https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true))

## 문제 설명
Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:  

Root: If node is root node.  
Leaf: If node is leaf node.  
Inner: If node is neither root nor leaf node.  

<br/>


### 입력 테이블
1. `BST`
   - `N`
   - `P` 

<br/>

### 풀이
```SQL
SELECT 
    N,
    CASE
        WHEN P IS NULL THEN 'Root'                
        WHEN N NOT IN (SELECT P FROM BST WHERE P IS NOT NULL) THEN 'Leaf' 
        ELSE 'Inner'                             
    END AS NodeType
FROM BST
ORDER BY N;      
```

<br/>

### 해석
1. 부모 노드 P이 NULL 이면 `Root`
2. 부모 노드 P가 NULL이 아니고, 있는 N (자식노드) 이면 `Leaf`
3. 그것도 아니면 `Inner`
