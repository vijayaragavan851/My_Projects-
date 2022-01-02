print("voting system mini project.")

#first getting the nominee names.
nominee1 = input("Enter the name of first nominee:")
nominee2 = input("Enter the name of second nominee:")
print("----------------------------------")

# initialize the vote count for both must be zero
nm1_votes = 0
nm2_votes = 0
total_votes = 0

voter_id = list(range(1,6))
no_of_voters = len(voter_id)

while True:
    if voter_id == []: # check when voter id is completed
        print("The voting session is over !!!")
        print("Total number of votes is",no_of_voters)
        print("Number of voters participated in the election",total_votes)
        if nm1_votes + nm2_votes == total_votes : 
           if nm1_votes > nm2_votes:
              print(f"{nominee1} has {nm1_votes} votes") 
              diff = nm1_votes - nm2_votes
              print(f"{nominee1} has won the election with {diff} majority votes")
              break
           elif nm2_votes > nm1_votes:
              print(f"{nominee2} has {nm2_votes} votes") 
              diff = nm2_votes - nm1_votes
              print(f"{nominee2} has won the election with {diff} majority votes")
              break
           else:
               print(f"{nominee1} has {nm1_votes} votes")
               print(f"{nominee2} has {nm2_votes} votes")
               print("Both are equal in votes,the government will decide who will rule.")
               break
    else:     
        voter = int(input("Enter your voter id number:"))
        if voter in voter_id:
           print("you are a voter")
           voter_id.remove(voter)
           print(f"To give the vote for {nominee1},press 1")
           print(f"To give the vote for {nominee2} press 2")
           print("----------------------------------------")
           vote = int(input("Enter your vote:"))
           if vote == 1:
              nm1_votes += 1
              total_votes += 1
              print(f"Thank you for your vote to the {nominee1}")
              print("------------------------------------------")
           elif vote == 2:
              nm2_votes += 1
              total_votes += 1
              print(f"Thank you for your vote to the {nominee2}")
              print("------------------------------------------")
           elif vote > 2:
              print("check your pressed key !!")
              print("------------------------------------------")
        else:
           print("you are not a voter or you are already participated in the election ")
 
