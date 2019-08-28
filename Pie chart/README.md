# PIE CHART ANIMATED VISUALIZATION - CHANGE PIECES SIZES OVER A TIME PERIOD
## Version 1.1

### Changelog:
	
>You can now change font size and font family
You can now create transparent-background output video
You can now change the resolution of the output video

### Instruction:

A pie chart compares percentages of different categories
The program runs with inputs from this JSON file (for how to properly use JSON, visit http://www.json.org/)
All the program's files must be put in a same folder (or you can use file paths, but that's clearly complex)

**Brief JSON guide:**
>JSON works under a simple format: keys (for naming) and values (for inputs) ("key": value)
Each key has a corresponding value. The keys must be put inside quotation marks. 
The value can be either numbers or strings (strings must be put inside quotation marks).
{} represents an object and [] represents a list. Every item in a list or an object must end with a comma (except the last item).
Spaces (includes blank lines) are optional and are only for the sake of readability (the machine ignores the spaces).

***ATTENTION: DO NOT DELETE OR ADD ANY FIELD OR KEY, WHICH MAY CAUSE MALFUNCTION. CHANGE THE CONTENT OF THE FILE AT YOUR OWN RISK.***

### Fields meaning
1. **title**: Title of the chart
2. **labels**: Labels of the categories
3. **colors**: Color of each pie piece that corresponds to the given label
4. **explode**: Margin of each pie piece that corresponds to the given label
5. **transparent**: Choose either "true" or "false". If "true" then the output will be in .mov, otherwise it will be in .mp4 (.mov may requires special softwares to run on some operating systems)
6. **data**: The figures that the program will handle in order to create a graph
The "data" field contains these items:
- **time_period**: The period that the figures is in. The period with be shown changing in the final video.
- **time_period_data**: The figures presented as a list. Each item in the list is the figure of a beginning category, correspondingly

***The program uses an interpolation algorithm to produce additional data in-between the given data to create a smooth animation (for instance: [1,5] -> [1,2,3,4,5]), so make sure that your data has a start point and an end point***
