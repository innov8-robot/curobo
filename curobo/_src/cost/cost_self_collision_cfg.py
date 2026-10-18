# SPDX-FileCopyrightText: Copyright (c) 2023-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

# Standard Library
from dataclasses import dataclass
from typing import Optional, Type

from curobo._src.cost.cost_base_cfg import BaseCostCfg
from curobo._src.cost.cost_self_collision import SelfCollisionCost

# CuRobo
from curobo._src.robot.types.self_collision_params import (
    SelfCollisionKinematicsCfg,
)


@dataclass
class SelfCollisionCostCfg(BaseCostCfg):
    class_type: Type[SelfCollisionCost] = SelfCollisionCost
    self_collision_kin_config: Optional[SelfCollisionKinematicsCfg] = None
    store_pair_distance: bool = False

    #: Extra clearance (meters) between two spheres below which the cost becomes active. It is added
    #: on top of the robot's self-collision buffer, split evenly between the two spheres of a pair.
    #: Set it on optimizer rollouts only, so that the optimizer keeps a margin that the feasibility
    #: check does not require: without it, a large weight drives trajectories to exact tangency and
    #: float noise then flips the binary feasibility metric.
    activation_distance: float = 0.0

    def __post_init__(self):
        return super().__post_init__()
