
import torchdata.datapipes as dp

class AddABunch(dp.iter.IterDataPipe):
    def __init__(self,q):
        self.q = [q]

    def __call__(self): list(self)

    def __iter__(self):
        for o in range(10): 
            self.q[0].put(o)
            yield o

if __name__=='__main__':
    from torch.multiprocessing import Pool, Process, set_start_method,Queue
    
    try:
        set_start_method('spawn')
    except RuntimeError:
        pass
    
    from torch.utils.data.dataloader_experimental import DataLoader2

    q = Queue()
    dl = DataLoader2(AddABunch(q),num_workers=1)
    list(dl)
    
    while not q.empty():
        print(q.get())
