from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary
from application.christmas_tree import *

def get_time_now():
    print(datetime.now())

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    get_time_now()
    plt.show()