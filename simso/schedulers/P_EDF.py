"""
Partitionned EDF using PartitionedScheduler.
"""
from simso.core.Scheduler import SchedulerInfo
from simso.utils import PartitionedScheduler
from simso.utils.PartitionedScheduler import decreasing_worst_fit ,decreasing_best_fit,decreasing_next_fit,decreasing_first_fit,first_fit,next_fit,worst_fit,best_fit
from simso.schedulers import scheduler

from simsogui.Global import GlobalData
from importlib import import_module

def getHeuristicFunc(heuristicStr):
    match heuristicStr:
        case 'decreasing_worst_fit':
            return decreasing_worst_fit
        case 'decreasing_best_fit':
            return decreasing_best_fit
        case 'decreasing_next_fit':
            return decreasing_next_fit
        case 'decreasing_first_fit':
            return decreasing_first_fit
        case 'first_fit':
            return first_fit
        case 'next_fit':
            return next_fit
        case 'worst_fit':
            return worst_fit
        case 'best_fit':
            return best_fit
        case default:
            return decreasing_first_fit

@scheduler("simso.schedulers.P_EDF")
class P_EDF(PartitionedScheduler):
    def init(self):
        print('heuristic: ', GlobalData.selected_heuristic)
        heuristicFunc = getHeuristicFunc(GlobalData.selected_heuristic)
        PartitionedScheduler.init(
            self, SchedulerInfo("simso.schedulers.EDF_mono"), heuristicFunc)
