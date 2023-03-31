# Cockroach


def cockroach_speed(speed_km_per_hour):
    speed_cm_per_second = int(speed_km_per_hour * 1000 * 100 / (60 * 60))
    return speed_cm_per_second


print(cockroach_speed(1.08))
print(cockroach_speed(1.09))
print(cockroach_speed(0))


# import codewars_test as test
# from solution import cockroach_speed

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(cockroach_speed(1.08),30)
#         test.assert_equals(cockroach_speed(1.09),30)
#         test.assert_equals(cockroach_speed(0),0)
