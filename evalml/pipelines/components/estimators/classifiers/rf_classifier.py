from sklearn.ensemble import RandomForestClassifier as SKRandomForestClassifier
from skopt.space import Integer

from evalml.model_family import ModelFamily
from evalml.pipelines.components.estimators import Estimator
from evalml.problem_types import ProblemTypes
from evalml.utils import deprecate_arg


class RandomForestClassifier(Estimator):
    """Random Forest Classifier."""
    name = "Random Forest Classifier"
    hyperparameter_ranges = {
        "n_estimators": Integer(10, 1000),
        "max_depth": Integer(1, 10),
    }
    model_family = ModelFamily.RANDOM_FOREST
    supported_problem_types = [ProblemTypes.BINARY, ProblemTypes.MULTICLASS,
                               ProblemTypes.TIME_SERIES_BINARY, ProblemTypes.TIME_SERIES_MULTICLASS]

    def __init__(self, n_estimators=100, max_depth=6, n_jobs=-1, random_state=None, random_seed=0, **kwargs):
        parameters = {"n_estimators": n_estimators,
                      "max_depth": max_depth,
                      "n_jobs": n_jobs}
        parameters.update(kwargs)
        random_seed = deprecate_arg("random_state", "random_seed", random_state, random_seed)
        rf_classifier = SKRandomForestClassifier(random_state=random_seed,
                                                 **parameters)
        super().__init__(parameters=parameters,
                         component_obj=rf_classifier,
                         random_seed=random_seed)
