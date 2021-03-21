# Report task 2.1

**Dmytro Steblyna**

## PART 1. The most popular hypervisors and the main differences between them:

**There are 2 different types of hypervisors that can be used for virtualization.**  

 
<br />
<img src="https://networklessons.com/wp-content/uploads/2018/12/hypervisor-type-1-type-2.png" alt="Hypervisors: type 1 vs type 2" width="650"/>

**Type 1:** a hypervisor is on bare metal. VM resources are scheduled directly to the hardware by the hypervisor. 

- VMware vSphere Hypervisor
- Microsoft Hyper-V
- Citrix XenServer
- KVM

**Type 2:** a hypervisor is hosted. VM resources are scheduled against a host operating system, which is then executed against the hardware.

- Oracle VirtualBox
- VMware Workstation Pro
- Parallels
- Qemu

**One of the best features of Type 1 hypervisors is that they allow for over-allocation of physical resources.**
With Type 1 hypervisors, you can assign more resources to your virtual machines than you have available. For example, if your server has 64 GB of RAM and 8 VMs, you can assign 12 GB of RAM to each of them. This totals to 96 GB of RAM, but the virtual machines themselves will not actually consume all 12 GB from the physical server. The VMs think they have 12 GB, when in reality they only use the amount of RAM they need to perform certain tasks.
