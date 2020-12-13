import os
import stepik_shop


if __name__ == '__main__':
    print(os.getcwd())
    print(stepik_shop.__name__)
    stepik_shop.to_db()
