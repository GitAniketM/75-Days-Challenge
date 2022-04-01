class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        result = []
        
        for i in range(len(transactions)):
            a = transactions[i]
            name, time, amount, city = a.split(',')
            if int(amount) > 1000:
                result.append(a)
                continue
                
            for j in range(len(transactions)):
                b = transactions[j]
                n,t,amt,cty = b.split(',')
                if i != j and n == name and cty != city and abs(int(time)-int(t)) <= 60:
                    result.append(a)
                    break
                    
        return result