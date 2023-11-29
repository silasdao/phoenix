from enum import Enum

import strawberry

from phoenix.core.model_schema import CONTINUOUS, Dimension


@strawberry.enum
class DimensionDataType(Enum):
    categorical = "categorical"
    numeric = "numeric"

    @classmethod
    def from_dimension(cls, dimension: Dimension) -> "DimensionDataType":
        data_type = dimension.data_type
        return cls.numeric if data_type in (CONTINUOUS,) else cls.categorical
