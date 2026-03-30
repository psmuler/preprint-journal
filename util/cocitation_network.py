import igraph as ig
from collections import Counter
from itertools import combinations

def build_cocitation(ref_lists):
    cnt = Counter()
    for refs in ref_lists:                      # refs: ある論文が引用しているIDの反復可能
        r = sorted(set(refs))                   # 同一論文内の重複と順序の影響を除去
        cnt.update(combinations(r, 2))          # 論文内ペアを加算（共引用1回）
    edges = [(a, b, w) for (a, b), w in cnt.items()]
    # g = ig.Graph.TupleList(edges, directed=False, weights=True, vertex_name_attr="name")
    # 単独出現ノード（どことも共引用していない）も頂点として入れたい場合は以下を有効化
    # all_refs = set().union(*map(set, ref_lists))
    # missing = all_refs - set(g.vs["name"])
    # if missing: g.add_vertices(list(missing))
    return g

# if __name__ == "__main__":
#     ref_list_sample =[
#         ["A", "B", "C"],
#         ["A", "C"],
#         ["B", "D"],
#         ["A", "D", "E"],
#         ["C", "E"],
#     ]
#     G = build_cocitation(ref_list_sample)
#     print(len(G.vs), len(G.es))
#     print(G.es["weight"])    # 共引用回数
    
import numpy as np
from scipy.sparse import coo_matrix
import igraph as ig
import time

def build_cocitation_from_edges(edge_list):
    # --- edge_list を numpy 配列に変換 ---
    # measure which part of the code takes time
    start = time.time()
    arr = np.array(edge_list, dtype=object)  # shape=(n,2)
    citing_ids = arr[:, 0]
    cited_ids  = arr[:, 1]
    print("Convert edge_list to numpy array:", time.time() - start)

    start = time.time()
    # --- 疎行列 A を直接構築 ---
    data = np.ones(len(edge_list), dtype=np.uint8)

    start = time.time()
    A = coo_matrix((data, (citing_ids, cited_ids)), dtype=np.int8)
    print("Build coarse matrix:", time.time() - start)

    start = time.time()
    # --- 共引用行列 C = A^T A を計算 ---
    C = (A @ A.T)
    print("Mutliply:", time.time() - start)
    
    start = time.time()
    C.setdiag(0)
    C.eliminate_zeros()
    print("Eliminate Diagonal:", time.time() - start)

    return C
    # # --- 自己共引用除外 ---
    # mask = C.row < C.col
    # edges = np.column_stack((C.row[mask], C.col[mask], C.data[mask]))

    # # --- index を id に戻す（vectorized） ---
    # edges_df = pd.DataFrame(edges, columns=["src", "dst", "weight"]).astype({"weight": int})
    # edges_df["src"] = cited_uniques[edges_df["src"].astype(int)]
    # edges_df["dst"] = cited_uniques[edges_df["dst"].astype(int)]

    # # --- igraph グラフへ変換 ---
    # g = ig.Graph.TupleList(edges_df.itertuples(index=False, name=None),
    #                        directed=False, weights=True, vertex_name_attr="name")

    # return g, C

if __name__ =="__main__":
    edges = [
        (1, 0), (1, 1), (1, 2),
        (2, 1), (2, 3), (2, 4),
        (3, 0), (3, 4)
    ]

    C = build_cocitation_from_edges(edges)
    print("Cocitation matrix shape:", C.todense())
    # print(len(g.vs), "nodes,", len(g.es), "edges")
    # print("weights:", g.es["weight"])