from datetime import timedelta

# criar um objeto do tipo timedelta
delta = timedelta(
    days = 50,
    seconds= 27,
    microseconds= 10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

print(delta)
print(delta.days)
print(delta.seconds)
print(delta.microseconds)