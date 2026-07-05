class Solution:
    def plantFlower(self, flowerbed, i, n):
        flowerbed[i] = 1
        n -= 1
        return n

    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 1:
                continue
            else:
                if i == 0:
                    if len(flowerbed) == 1:
                        n = self.plantFlower(flowerbed, i, n)
                    elif flowerbed[i + 1] == 1:
                        continue
                    else:
                        n = self.plantFlower(flowerbed, i, n)
                        continue
                elif i == (len(flowerbed) - 1):
                    if flowerbed[i - 1] == 1:
                        break
                    else:
                        n = self.plantFlower(flowerbed, i, n)
                else:
                    if flowerbed[i - 1] == 1 or flowerbed[i + 1] == 1:
                        continue
                    else:
                        n = self.plantFlower(flowerbed, i, n)
        if n == 0:
            return True
        else:   
            return False
