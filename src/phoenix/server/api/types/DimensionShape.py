from enum import Enum

import strawberry

from phoenix.core.model_schema import CONTINUOUS, Dimension


@strawberry.enum
class DimensionShape(Enum):
    continuous = "continuous"
    discrete = "discrete"

    @classmethod
    def from_dimension(cls, dim: Dimension) -> "DimensionShape":
        data_type = dim.data_type
        return cls.continuous if data_type in (CONTINUOUS,) else cls.discrete
