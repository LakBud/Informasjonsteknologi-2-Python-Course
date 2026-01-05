# def sum_oddetallene(n: int) -> int:
#     total: int = 0
#     for i in range(0, n):
#         if i % 3 == 0:
#             total += i 
#     return total

# print(f"Summen av oddtallene: {sum_oddetallene(10)} | Summen i kvadrat: {sum_oddetallene(10)**2}")


# b = 4
# c = 5
# for a in range(2,5):
#     print(c)
#     b -= 1
#     c += b


# l = [2,1,4,5,3,2]
# s = ""
# l.sort()
# l = l[::-1]
# for t in l:
#     s += f"{t}, "
# print(s[:-2])


# class Klasse:
#     def __init__(self, k_navn: str):
#         self.k_navn = k_navn
    
#     def m_1(self):
#         print("Hei på deg")
        
#     def m_2(self):
#         self.m_1()


# class Barn(Klasse):
#     def __init__(self, k_navn: str):
#         super().__init__(k_navn)
    
#     def m_1(self):
#         super().m_1()
    
#     def m_2(self):
#         super().m_1()
#         print(f"{self.k_navn}")

# k = Klasse("Super")
# b = Barn("Barn")

# k.m_2()
# b.m_1()
# b.m_2()


