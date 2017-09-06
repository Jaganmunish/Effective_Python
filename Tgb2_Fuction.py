import pandas as pd
import numpy as np


codreg = [3, 4, 3, 4, 4, 1, 3, 3, 3, 3, 4, 2, 2, 2, 2, 3, 3, 1, 3, 1, 2, 2, 3, 2, 4, 2, 4, 1, 1, 4, 1, 3, 2, 2, 3,
          4, 1, 1, 3, 2, 3, 3, 4, 1, 3, 4, 3, 2, 4, 4, 4]
codreg2 = pd.DataFrame({'codreg': codreg})
codreg2.index = range(1, len(codreg2) + 1)
codreg2['state'] = codreg2.index

def tgb2_read(file,out_file):
    file['startdate'] = startdate
    file['enddate'] = enddate
    file['day2'] = day2
    file['bday'] = bday2
    file['eday'] = eday2

    file['STARTER'] = file.nsys * 7 + 391
    file['npm'] = np.where((file.dma == 517) & (file.lpm == 'Y'), 'Y', file.npm)

    file['ed'] = np.where(file.edu < 12, 1, np.where(file.edu == 12, 2, np.where((file.edu > 12) & (file.edu < 16), 3,
                                                                                 np.where(file.edu > 15, 4, 0))))
    file['hisp'] = np.where(file.spn == 1, 2, 1)
    file['hhsz'] = np.where(file.hhsz > 5, 5, file.hhsz)
    file['ahoh'] = np.where(file.ahoh > 100, 100, file.ahoh)
    out_filet_file = pd.merge(tgb2, codreg2, how='left', on=['state'])
    return out_file


def func(x):
    if 1 <= x <= 24:
        return '1'
    elif 25 <= x <= 34:
        return '2'
    elif 35 <= x <= 44:
        return '3'
    elif 45 <= x <= 54:
        return '4'
    elif 55 <= x <= 64:
        return '5'
    return '6'

out_file['hoh'] = out_file['ahoh'].apply(func)
out_file['Index'] = out_file.index
out_file['p2p']=0


for x in range(1, 16):
    out_file['posF'+str(x)]=0
    out_file['posM'+str(x)]=0 

out_file['posF1']=np.where(out_file.FEMALES>0,out_file.STARTER,0)
out_file['posM1']=np.where(out_file.MALES>0,out_file.STARTER+(3*out_file.FEMALES)+(3*out_file.WW),0)
for i in range(2,16):
    out_file['posF'+str(i)]=np.where(out_file.FEMALES>(i-1),out_file['posF'+str(i-1)]+3,0)
    out_file['posM'+str(i)]=np.where(out_file.MALES>(i-1),out_file['posM'+str(i-1)]+3,0)

lines1 = open(inpath+infile1).read().splitlines()
lines1 = pd.DataFrame({'col': lines1})
lines1.drop(lines1.index[:1], inplace=True)
lines1=lines1.reset_index(drop='index')
out_file=out_file.join(lines1)

def cat_name(files, pos_ch, chr1 = ' ' , ):
    for f in range(1, 16):
        pos = tgb11[pos + str(f)]
        ln = []
        for row, i in zip(files['col'], range(0, len(lines1.col))):
            ln.append(row[pos[i] - 1:pos[i] + 2])
        ln = pd.DataFrame({'femage' + str(f): ln})
        ln[['femage' + str(f)]] = ln[['femage' + str(f)]].apply(pd.to_numeric)
        ln['Index'] = ln.index
        tgb11 = pd.merge(tgb11, ln, how='left', on=['Index'])






