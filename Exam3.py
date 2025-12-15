file=open('input.txt','r')

for line in file:
  line=line.strip()
  parts=line.split()
  # dd stands for degree of difficukty

  name=parts[0]
  dd=float(parts[1])
  scores=[] #judges scores
  
  for i in range(2,9):
    scores.append(float(parts[i]))

  highest=max(scores)
  lowest=min(scores)
  scores.remove(highest)
  scores.remove(lowest)
  total=0
  for score in scores:
    total+=score
  average=total/len(scores)
  final_score=average*dd
  print(f"{name}'\t' {str(dd)} '\t' {str(round(final_score,1))} ")
  file.close()