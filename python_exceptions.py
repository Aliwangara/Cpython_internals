

class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

def check(age):
    if age < 0:
        raise ValidationError("age cannot be negative")
    return age

# Block 1: the order of try / except / else / finally
def run(value):
    try:
        print("trying")
        result = 10 / value
    except ZeroDivisionError:
        print("except")
    else:
        print("else:", result)
    finally:
        print("finally")

run(2) # will print else 5
print("---")
run(0) # will raise a zero divison error except

print("---")

# Block 2: catching by parent class
try:
    check(-5)
except AppError as e:
    print("caught as AppError:", e) # Caught as app error: age cannot be negative

print(issubclass(ValidationError, Exception)) #TRUE
print(ValidationError.__mro__) # will order starting with Validation then App error

print("---")

# Block 3: the order of except clauses
try:
    check(-5)
except Exception:
    print("first: Exception") # first:Exception
except ValidationError:
    print("second: ValidationError") # Doesnt reach here