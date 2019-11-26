import snap


class CesnaUtil:

    @staticmethod
    def load_nid_attrh_from_nidkh(
            nidv, # TIntV
            attr_filename: str, # file with attribute names
            raw_nid_attrh, # TIntStrH
            node_names_h): # TStrHash<TFltV>
        pass

    @staticmethod
    def filter_low_entropy(
            raw_nid_attrh, # TIntStrH
            nid_attr_h, # THash<TInt, TIntV>
            raw_feat_name_h, # THash<TInt, TIntV>
            feat_name_h, # TIntStrH
            min_feat_frac: float): # minimal fraction to keep feature
        pass


class Cesna:

    def __init__(self,
            graph: snap.PUNGraph,
            node_attributes: dict,
            initial_communities_count: int=10,
            seed: int=10):
        self.graph = graph
        self.node_attributes = node_attributes
        self.communities_count = initial_communities_count
        self.seed = seed

    def find_communities(self,
            comm_max: int,
            comm_min :int,
            comm_div: int,
            step_alpha: float=0.3,
            step_beta: float=0.1,
            output_prefix: str="",
            use_bic: float=false,
            test_split: float=0.1) -> int:
        return -1

    def neighbor_communities_init(self,
            number_of_communities_to_search: int):
        if number_of_communities_to_search == -1:
            # todo: infer communities
            pass
        else:
            pass

    def set_attribute_weight(self, weights: [float]):
        self.attr_weights = weights
        pass

    def set_lasso_coef(self, lasso_coef: float):
        self.lasso_coef = lasso_coef
        pass

    def mle_grad_ascent(self,
            threshold: float,
            max_iterations: int,
            plot_name,
            step_alpha: float=0.3,
            step_beta: float=0.1) -> int:
        return -1

    def get_communities_weights(self,
            estimated_community_weights, # [TFltV]
            wck): # [TFltV]
        pass

    def read(self, filename: str):
        pass

    def write(self, filename_prefix: str):
        pass
