processed = set()
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticket_map = {}
        ticket_counts = {}
        for i in tickets:
            start = i[0]
            end = i[1]
            if (start, end) not in ticket_counts:
                ticket_counts[(start, end)] = 0
            ticket_counts[(start, end)] += 1
            if start not in ticket_map:
                ticket_map[start] = []
            ticket_map[start] += [end]
        ret = []
        self.find_route(ticket_counts, ticket_map, {}, ["JFK"], len(tickets), ret)
        tosort = {}
        for i in ret:
            tosort[str(i)] = i
        keys = tosort.keys()
        keys = sorted(keys)
        return tosort[keys[0]]

    def find_route(self, ticket_counts, ticket_map, used, path, depth, ret):
        if (str(path), depth, str(used)) in processed:
            return
        processed.add((str(path), depth, str(used)))

        if depth == 0:
            return path
        else:
            curr = path[-1]
            if curr in ticket_map:
                for i in ticket_map[curr]:
                    if (curr, i) in used and used[(curr, i)] == ticket_counts[(curr, i)]:
                        continue
                    else:
                        if (curr, i) not in used:
                            used[(curr, i)] = 0
                        used[(curr, i)] += 1
                        tmp = self.find_route(ticket_counts, ticket_map, used, path+[i], depth-1, ret)
                        if tmp:
                            ret += [tmp]
                        used[(curr, i)] -= 1


s = Solution()
print s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print s.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]])
print s.findItinerary([["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]])
