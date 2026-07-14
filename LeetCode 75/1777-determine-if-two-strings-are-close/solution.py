class Solution:
    def closeStrings(self, word1, word2):
        arr_dict1 = {}
        arr_dict2 = {}
        key_list1 = []
        key_list2 = []
        val_list1 = []
        val_list2 = []

        for a in word1:
            if a in arr_dict1:
                arr_dict1[a] += 1
            else:
                arr_dict1[a] = 1

        for a in word2:
            if a in arr_dict2:
                arr_dict2[a] += 1
            else:
                arr_dict2[a] = 1

        for key, val in arr_dict1.items():
            key_list1.append(key)
            val_list1.append(val)

        for key, val in arr_dict2.items():
            key_list2.append(key)
            val_list2.append(val)

        if sorted(key_list1) == sorted(key_list2) and sorted(val_list1) == sorted(val_list2):
            return True
        else:
            return False
