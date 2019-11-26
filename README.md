# community-detection
Community detection algorithms for attributed graphs (Probabilistic models)

## Roadmap
Roadmap:

    1. [ ] Try to understand what's going on in algorithm
    2. [ ] Rewrite implementation from agmattr in python using snap
    3. [ ] Prepare dataset suitable in format to cesna, but different than 1912
    4. [ ] Prepare presentation
    5. [ ] Write report

## Papers
[google disk](https://drive.google.com/drive/folders/1BtWmRUWvZIepF6DBLkTN3KMiKqUmW25Z?usp=sharing)


## Original implementation of CESNA
[SNAP](https://github.com/snap-stanford/snap)
[SNAP-project](http://snap.stanford.edu/)
[SNAP-datasets](http://snap.stanford.edu/data/index.html)

In fact we only need the following functions:
 - [x] methods to read edges (borrowed from TAGMUtil::LoadEdgeListStr)
 - [ ] TCesnaUtil::LoadNIDAttrHFromNIDKH
 - [ ] TCesnaUtil::FilterLowEntropy
 - [ ] TCesna::constructor
 - [ ] TCesna::FindComs
 - [ ] TCesna::NeighborComInit
 - [ ] TCesna::SetWeightAttr
 - [ ] TCesna::LassoWeight
 - [ ] TCesna::MLEGradAscent
 - [ ] TCesna::GetCmtyVV
 - [ ] method to write down results


Class where Cesna is implemented: snap/snap-adv/agmattr.cpp
Class where example is provided: snapp/examples/cesna
