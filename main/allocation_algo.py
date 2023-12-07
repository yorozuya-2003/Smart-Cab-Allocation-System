import numpy as np
from scipy.optimize import linear_sum_assignment


class CabAllocationAlgorithm:
    def __init__(self):
        self.riders = []
        self.drivers = []

    def add_rider(self, rider_id, location):
        self.riders.append((rider_id, location))

    def add_driver(self, driver_id, location):
        self.drivers.append((driver_id, location))

    def allocate_cabs(self):
        # hungarian algo for optimal assignment
        cost_matrix = np.array([[self.calculate_distance(rider[1], driver[1]) for driver in self.drivers] for rider in self.riders])
        row_indices, col_indices = linear_sum_assignment(cost_matrix)

        # tracking allocated drivers to riders
        allocation_dict = {self.riders[row][0]: self.drivers[col][0] for row, col in zip(row_indices, col_indices)}

        # unallocated cab situation
        unallocated_riders = set(rider[0] for rider in self.riders) - set(allocation_dict.keys())
        for rider_id in unallocated_riders:
            allocation_dict[rider_id] = "cab not available at the moment"

        return allocation_dict

    def calculate_distance(self, location1, location2):
        # todo: need to use real time street path based distance calculation
        return ((location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2) ** 0.5


if __name__ == "__main__":
    cab_system = CabAllocationAlgorithm()

    # example test case
    cab_system.add_rider(1, (1, 1))
    cab_system.add_rider(2, (5, 5))
    cab_system.add_rider(3, (3, 3))

    cab_system.add_driver(101, (2, 2))
    cab_system.add_driver(102, (4, 4))

    allocation_result = cab_system.allocate_cabs()
    print(f'allocation result: {allocation_result}')
