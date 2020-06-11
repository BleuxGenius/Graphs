import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(1, num_users + 1):
            self.add_user(f"User {user}")

        # Create friendships
        # list of possible friendships

        maybe_friendships = []
        for user_id in self.users:
            # collecting the usersID in the self.users
            for friend_id in range(user_id + 1, self.last_id + 1):
                maybe_friendships.append((user_id, friend_id))
                #  we have every friendship that can happen
                random.shuffle(maybe_friendships)
                # shuffle it and get the first few
                #  loop over every friendship
                # divide by 2 since the friendships create 2 friendships
                for friend in range(num_users * avg_friendships // 2):
                    friendship = maybe_friendships[friend]
                    print(friendship)
                    #  call the add_Frienship on all the friends that we can get 
                    self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        if user_id not in self.users:
            return None
            # check the adjacent(neighboring) sides of the graph with bfs (breadth - first - search)
            # bfs is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root and explores all of the neighbor nodes/vertex.
        queue = Queue()
        queue.enqueue([user_id])
        #  the queue is not empty
        while len(queue) > 0:
            # dequeue to path variable
            bfs_path = queue.dequeue()
            # set the new user id to the last item in the path 
            vertex = bfs_path[-1] # last vertex in path
                # check if the new vertex is not visitied 
            if vertex not in visited:
                visited[vertex] = bfs_path
                print(visited)
                    # loop over each id in the friendships at the index of the new user id 
                for next_vertex in self.friendships[vertex]:
                    if next_vertex not in visited:
                        # create a copy of the path 
                        new_path = bfs_path.copy()
                        # appened the friend id to the copied path
                        new_path.append(next_vertex)
                        # enqueue the copy of the path
                    queue.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
