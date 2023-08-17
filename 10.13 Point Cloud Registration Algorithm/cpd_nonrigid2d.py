from probreg import cpd
from probreg import callbacks
import matplotlib.pyplot as plt
import utils
from pathlib import Path

caminho = Path('10.13 Point Cloud Registration Algorithm')

source, target = utils.prepare_source_and_target_nonrigid_2d(caminho / 'fish_source.txt',
                                                             caminho / 'fish_target.txt')
cbs = [callbacks.Plot2DCallback(source, target)]
print(len(cbs))
tf_param, _, _ = cpd.registration_cpd(source, target, 'nonrigid',
                                      callbacks=cbs)
plt.show()