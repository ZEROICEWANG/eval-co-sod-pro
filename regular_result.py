import pandas as pd
import numpy as np


def main():
    path='./result.txt'
    with open(path, 'r') as f:
        lines = f.readlines()

    result_list=[]
    keys=[]
    for line in lines:
        msg=line.split('] ')[-1]
        tag,scores=msg.split(' (')
        dataset,scores=scores.split('):')
        scores=scores.strip().split('||')
        score_list=[]
        for score in scores[:-1]:
            score_list.append(float(score.strip().split(' ')[0]))
        if tag in keys:
            result_list[-1]=result_list[-1]+score_list
        else:
            result_list.append(['',tag,'','','']+score_list)
            keys.append(tag)
    results=np.array(result_list)
    dataF=pd.DataFrame(results)
    writer=pd.ExcelWriter('./result.xlsx')
    dataF.to_excel(writer,'Sheet1',index=False,header=None)
    writer.save()


if __name__ == '__main__':
    main()
