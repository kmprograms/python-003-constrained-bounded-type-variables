# def concatenate_and_upper(s1: str, s2: str) -> str:
#     return (s1 + s2).upper()

def concatenate_and_upper[T: (str, bytes)](s1: T, s2: T) -> T:
    return (s1 + s2).upper()


class Worker:
    pass

class Student(Worker):
    pass

def do_worker_action[T: Worker](worker: T) -> None:
    print(worker)

def main() -> None:
    print(concatenate_and_upper('ala', ' ma kota'))
    print(concatenate_and_upper(b'ala', b' ma kota'))
    # print(concatenate_and_upper(10, 20))

    do_worker_action(Worker())
    do_worker_action(Student())
    do_worker_action(10)

if __name__ == '__main__':
    main()