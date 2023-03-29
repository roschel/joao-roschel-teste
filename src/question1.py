from typing import List


class Contract:
    def __init__(self, id: int, debt: int):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    @staticmethod
    def get_top_N_open_contracts(
            open_contracts: List[Contract],
            renegotiated_contracts: List[int],
            top_n: int
    ) -> List[int]:
        result = list((contract for contract in open_contracts if contract.id not in renegotiated_contracts))
        result.sort(key=lambda x: x.debt, reverse=True)
        return [contract.id for contract in result][:top_n]


contracts = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5),
    Contract(6, 10),
    Contract(7, 28),
    Contract(8, 2),
    Contract(9, 50),
    Contract(10, 100),
    Contract(11, 789),
    Contract(12, 80),
    Contract(13, 90),
    Contract(14, 1),
]

renegotiated = [3]
top_n = 3

result = Contracts.get_top_N_open_contracts(open_contracts=contracts, renegotiated_contracts=renegotiated, top_n=top_n)
print(result)
