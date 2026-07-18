class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        stack = []

        # Zip position and speed, sort by reverse position
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        print(cars)

        # Iterate over each car
        for car in cars:
            print(stack)
            # If stack is empty, start a new fleet and append car to it
            while stack:
                car_pos = car[0]
                car_speed = car[1]
                next_car_pos = stack[0][0]
                next_car_speed = stack[0][1]
                # Time = Distance / Speed
                car_time_to_target = (target - car_pos) / car_speed
                next_car_time_to_target = (target - next_car_pos) / next_car_speed
                # If next_car reaches target faster than car, it makes a new fleet and we empty the stack
                if next_car_time_to_target < car_time_to_target:
                    stack = []
                    fleets += 1
                # If next_car reaches target slower than car, it joins the current fleet on the stack
                else:
                    break
            stack.append(car)
        return fleets

