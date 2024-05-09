from z3 import *

# Give a chip design containing two power components and ten regular components satisfying the
# following constraints:
#   •   Both the width and the height of the chip is 30.
#   •   The power components have size 4 × 3 and the ten other regular components have a size 4 × 5,
#       4 × 6, 5 × 20, 6 × 9, 6 × 10, 6 × 11, 7 × 8, 7 × 12, 10 × 10, and 10 × 20.
#   •   All components may be turned 90°, but may not overlap.
#   •   In order to get power, all regular components should directly be connected to a power com-
#       ponent, that is, an edge of the component should have a part of length > 0 in common with
#       an edge of the power component.
#   •   Due to limits on heat production the power components should be not too close: their centres
#       should differ at least 16 in either the x direction or the y direction (or both).
