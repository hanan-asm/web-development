class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {}
        players = set()

        for winner, loser in matches:
            lost[loser] = lost.get(loser, 0) + 1
            players.add(winner)
            players.add(loser)

        losses = []
        loss = []

        for player in players:
            if lost.get(player, 0) == 0:
                losses.append(player)
            elif lost[player] == 1:
                loss.append(player)

        return [sorted(losses), sorted(loss)]
