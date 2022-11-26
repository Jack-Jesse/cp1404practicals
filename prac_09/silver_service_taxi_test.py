from silver_service_taxi import SilverServiceTaxi

my_silver_service = SilverServiceTaxi("Prius 1", 100, 2)
# my_silver_service.drive(40)
# print(my_silver_service)
# my_silver_service.start_fare()
# my_silver_service.drive(100)
# print(my_silver_service)
my_silver_service.drive(18)
print(my_silver_service)
print(f"${my_silver_service.get_fare():,.2f}")
