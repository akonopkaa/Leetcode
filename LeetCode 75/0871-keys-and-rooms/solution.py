class Solution:
    def canVisitAllRooms(self, rooms):
        queue = [0]
        visited = set()
        while queue:
            room = queue.pop(0)
            if room in visited:
                continue
            visited.add(room)
            for key in rooms[room]:
                queue.append(key)
        return len(rooms) == len(visited)
