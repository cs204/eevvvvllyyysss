import pytest
from jar import Jar

def test_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("10")

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(6)  # Превышает емкость

    jar.deposit(5)
    assert jar.size == 10  # Достигнута максимальная емкость

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)  # Недостаточно печений для удаления

    jar.withdraw(3)
    assert jar.size == 0  # Все печенья удалены

def test_str():
    jar = Jar(10)
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_capacity():
    jar = Jar(15)
    assert jar.capacity == 15

if __name__ == "__main__":
    pytest.main()
