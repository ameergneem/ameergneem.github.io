var models = [
  {
    "model_name": "19th Century",
    "id": "1",
    "positive": 63,
    "neutral": 2,
    "negative": 68,
    "Count": 133
  },
  {
    "model_name": "1900s",
    "id": "2",
    "positive": 8,
    "neutral": 0,
    "negative": 1,
    "Count": 9
  },
  {
    "model_name": "1910s",
    "id": "3",
    "positive": 9,
    "neutral": 0,
    "negative": 4,
    "Count": 13
  },
  {
    "model_name": "1920s",
    "id": "4",
    "positive": 5,
    "neutral": 1,
    "negative": 7,
    "Count": 13
  },
  {
    "model_name": "1930s",
    "id": "5",
    "positive": 6,
    "neutral": 0,
    "negative": 3,
    "Count": 9
  },
  {
    "model_name": "1940s",
    "id": "6",
    "positive": 14,
    "neutral": 0,
    "negative": 9,
    "Count": 23
  },
  {
    "model_name": "1950s",
    "id": "7",
    "positive": 13,
    "neutral": 0,
    "negative": 10,
    "Count": 23
  },
  {
    "model_name": "1960s",
    "id": "8",
    "positive": 20,
    "neutral": 1,
    "negative": 17,
    "Count": 38
  },
  {
    "model_name": "1970s",
    "id": "9",
    "positive": 24,
    "neutral": 4,
    "negative": 34,
    "Count": 62
  },
  {
    "model_name": "1980s",
    "id": "10",
    "positive": 55,
    "neutral": 6,
    "negative": 44,
    "Count": 105
  },
  {
    "model_name": "1990s",
    "id": "11",
    "positive": 99,
    "neutral": 4,
    "negative": 85,
    "Count": 188
  },
  {
    "model_name": "2000s",
    "id": "12",
    "positive": 122,
    "neutral": 6,
    "negative": 125,
    "Count": 253
  },
  {
    "model_name": "2010s",
    "id": "13",
    "positive": 291,
    "neutral": 22,
    "negative": 353,
    "Count": 666
  }
];
models = models.map(i => {
  i.model_name = i.model_name;
	return i;
});

var container = d3.select('#cont2'),
    width = 700,
    height = 300,
    margin = {top: 30, right: 100, bottom: 30, left: 50},
    barPadding = .2,
    axisTicks = {qty: 5, outerSize: 0, dateFormat: '%m-%d'};

var svg = container
   .append("svg")
   .attr("width", width)
   .attr("height", height)
   .append("g")
   .attr("transform", `translate(${margin.left},${margin.top})`);


   svg.append("circle").attr("cx",570).attr("cy",130).attr("r", 6).style("fill", "green")
   svg.append("circle").attr("cx",570).attr("cy",160).attr("r", 6).style("fill", "orange")
   svg.append("circle").attr("cx",570).attr("cy",190).attr("r", 6).style("fill", "red")
   svg.append("text").attr("x", 590).attr("y", 130).text("Positive").style("font-size", "15px").attr("alignment-baseline","middle")
   svg.append("text").attr("x", 590).attr("y", 160).text("Neutral").style("font-size", "15px").attr("alignment-baseline","middle")
   svg.append("text").attr("x", 590).attr("y", 190).text("Negative").style("font-size", "15px").attr("alignment-baseline","middle")



var xScale0 = d3.scaleBand().range([0, width - margin.left - margin.right]).padding(barPadding);
var xScale1 = d3.scaleBand();
var yScale = d3.scaleLinear().range([height - margin.top - margin.bottom, 0]);

var xAxis = d3.axisBottom(xScale0).tickSizeOuter(axisTicks.outerSize);
var yAxis = d3.axisLeft(yScale).ticks(axisTicks.qty).tickSizeOuter(axisTicks.outerSize);

xScale0.domain(models.map(d => d.model_name));
xScale1.domain(['positive', 'neutral','negative']).range([0, xScale0.bandwidth()]);
yScale.domain([0, d3.max(models, d => d.negative+100)]);

var model_name = svg.selectAll(".model_name")
  .data(models)
  .enter().append("g")
  .attr("class", "model_name")
  .attr("transform", d => `translate(${xScale0(d.model_name)},0)`);

/* Add positive bars */
model_name.selectAll(".bar.positive")
  .data(d => [d])
  .enter()
  .append("rect")
  .attr("class", "bar positive")
.style("fill","green")
  .attr("x", d => xScale1('positive'))
  .attr("y", d => yScale(d.positive))
  .attr("width", xScale1.bandwidth())
  .attr("height", d => {
    return height - margin.top - margin.bottom - yScale(d.positive)
  });
  
/* Add neutral bars */
model_name.selectAll(".bar.neutral")
  .data(d => [d])
  .enter()
  .append("rect")
  .attr("class", "bar neutral")
.style("fill","yellow")
  .attr("x", d => xScale1('neutral'))
  .attr("y", d => yScale(d.neutral))
  .attr("width", xScale1.bandwidth())
  .attr("height", d => {
    return height - margin.top - margin.bottom - yScale(d.neutral)
  });
 
 model_name.selectAll(".bar.negative")
  .data(d => [d])
  .enter()
  .append("rect")
  .attr("class", "bar negative")
.style("fill","red")
  .attr("x", d => xScale1('negative'))
  .attr("y", d => yScale(d.negative))
  .attr("width", xScale1.bandwidth())
  .attr("height", d => {
    return height - margin.top - margin.bottom - yScale(d.negative)
  });
 

  svg.append('text').attr('id','barsText').attr('fill', 'black')
  .attr('class', 'label')
  .attr('x', width / 2 + margin)
  .attr('y', height + margin * 1.7)
  .attr('text-anchor', 'middle')
  .text("Number of Reviews")
  
  
     svg.append('text').attr('id','barsText').attr('fill', 'black')
      .attr('class', 'title')
      .attr('x', width/2  - 20)
      .attr('y', -20)
      .attr('text-anchor', 'middle')
      .style("font-size", "100%")
      .style("text-decoration", "underline") 
      .text("IBM Watson Sentement Analysis Results (New York Times)")
 
// Add the X Axis
svg.append("g")
   .attr("class", "x axis")
   .attr("transform", `translate(0,${height - margin.top - margin.bottom})`)
   .call(xAxis);

// Add the Y Axis
svg.append("g")
   .attr("class", "y axis")
   .call(yAxis); 