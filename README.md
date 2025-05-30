# ICEUP Project

In the Iceberg Contribution to ECCO Upgrade and Performance (ICEUP) project I updated the freshwater (FW) runoff forcing of ECCOV4 to include more realistic forcing from the Greenland icesheet. The contribution from icebergs are distributed spatially such that the freshwater flux is not only at the glacier outlet but instead where the icebergs melt.
I ran ECCOV4r4 with this new runoff forcing on the P-cluster over a 26 year period. In this way the effect on temperature, salinity, current strength, and sea ice of the increased FW flux from Greenland is analysed.

## Files and folders in this project repository

This template provides the following suggested organizaiton structure for the project repository, but each project team is free to organize their repository as they see fit.

* **`notebooks/`**
<br> Here are the notebooks that I used to generate the runoff file (`Greenland_FW.ipynb`) and to plot the result of the ECCOV4r4 simulation with the new forcing (`lookatoutput.ipynb`).
* **`data/`**
<br> Data used to generate the runoff file are located in this directory.
`Dataverse/` are csv files of the runoff, basal melt, and solid discharge at 267 glacier outlets from GEUS,  https://doi.org/10.22008/FK2/BOVBVR. `00_GlacierGates.gpkg` contains the coordinates of the glacier gates. `altiberg/` contains netcdf files of the iceberg FW data from altiberg, https://doi.org/10.13140/2.1.4518.1765.


### The problem

Provide a few sentences describing the problem are you going to explore. If this is a technical exploration of software or data science methods, explain why this work is important in a broader context and specific applications of this work.

## Data and Methods

### Data

Briefly describe and provide citations for the data that will be used (size, format, how to access).

### Existing methods

How would you or others traditionally try to address this problem? Provide any relevant citations to prior work.

### Proposed methods/tools

What new approaches would you like to implement for addressing your specific question(s) or application(s)?

Will your project use machine learning methods? If so, we invite you to create a [model card](model-card.md)!

### Additional resources or background reading

Optional: links to manuscripts or technical documents providing background information, context, or other relevant information.

## Project goals and tasks

### Project goals

List the specific project goals or research questions you want to answer. Think about what outcomes or deliverables you'd like to create (e.g. a series of tutorial notebooks demonstrating how to work with a dataset, results of an anaysis to answer a science question, an example of applying a new analysis method, or a new python package).

* Goal 1
* Goal 2
* ...

### Tasks

What are the individual tasks or steps that need to be taken to achieve each of the project goals identified above? What are the skills that participants will need or will learn and practice to complete each of these tasks? Think about which tasks are dependent on prior tasks, or which tasks can be performed in parallel.

* Task 1 (all team members will learn to use GitHub)
* Task 2 (team members will use the scikit-learn python library)
  * Task 2a (assigned to team member A)
  * Task 2b (assigned to team member B)
* Task 3
* ...

## Project Results

Use this section to briefly summarize your project results. This could take the form of describing the progress your team made to answering a research question, developing a tool or tutorial, interesting things found in exploring a new dataset, lessons learned for applying a new method, personal accomplishments of each team member, or anything else the team wants to share.

You could include figures or images here, links to notebooks or code elsewhere in the repository (such as in the [notebooks](notebooks/) folder), and information on how others can run your notebooks or code.
