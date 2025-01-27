"""
Partitionned EDF using PartitionedScheduler.
"""
from simso.core.Scheduler import SchedulerInfo
from simso.utils import PartitionedScheduler
from simso.schedulers import scheduler
from simso.utils.PartitionedScheduler import decreasing_worst_fit ,decreasing_best_fit,decreasing_next_fit,decreasing_first_fit,first_fit,next_fit,worst_fit,best_fit
from simsogui.Global import GlobalData

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

@scheduler("simso.schedulers.P_RM")
class P_RM(PartitionedScheduler):
    def init(self):
        print('heuristic: ', GlobalData.selected_heuristic)
        heuristicFunc = getHeuristicFunc(GlobalData.selected_heuristic)
        PartitionedScheduler.init(
            self, SchedulerInfo("simso.schedulers.RM_mono"), heuristicFunc)

    # def packer(self):
    #     # First Fit
    #     cpus = [[cpu, 0] for cpu in self.processors]
    #     for task in self.task_list:
    #         m = cpus[0][1]
    #         j = 0
    #         # Find the processor with the lowest load.
    #         for i, c in enumerate(cpus):
    #             if c[1] < m:
    #                 m = c[1]
    #                 j = i

    #         # Affect it to the task.
    #         self.affect_task_to_processor(task, cpus[j][0])

    #         # Update utilization.
    #         cpus[j][1] += float(task.wcet) / task.period
    #     return True
