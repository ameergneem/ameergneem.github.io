var models = [
  {
    "model_name":"OneStar",
    "positive":433,
    "neutral":84,
    "negative":2311
  },
  {
    "model_name":"TwoStars",
    "positive":1063,
    "neutral":66,
    "negative":2948

  },
  {
    "model_name":"ThreeStars",
    "positive":4222,
    "neutral":221,
    "negative":3741

  },
  {
    "model_name":"FourStars",
    "positive":11585,
    "neutral":489,
    "negative":5079

  },
  {
    "model_name":"FiveStars",
    "positive":16260,
    "neutral":702,
    "negative":5508

  }
];
models = models.map(i => {
  i.model_name = i.model_name;
	return i;
});

var container = d3.select('#d3id'),
    width = 500,
    height = 300,
    margin = {top: 30, right: 20, bottom: 30, left: 50},
    barPadding = .2,
    axisTicks = {qty: 5, outerSize: 0, dateFormat: '%m-%d'};

var svg = container
   .append("svg")
   .attr("width", width)
   .attr("height", height)
   .append("g")
   .attr("transform", `translate(${margin.left},${margin.top})`);

var xScale0 = d3.scaleBand().range([0, width - margin.left - margin.right]).padding(barPadding);
var xScale1 = d3.scaleBand();
var yScale = d3.scaleLinear().range([height - margin.top - margin.bottom, 0]);

var xAxis = d3.axisBottom(xScale0).tickSizeOuter(axisTicks.outerSize);
var yAxis = d3.axisLeft(yScale).ticks(axisTicks.qty).tickSizeOuter(axisTicks.outerSize);

xScale0.domain(models.map(d => d.model_name));
xScale1.domain(['positive', 'neutral','negative']).range([0, xScale0.bandwidth()]);
yScale.domain([0, d3.max(models, d => d.positive)]);

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
  .text("number of reviews")
  
  
     svg.append('text').attr('id','barsText').attr('fill', 'black')
      .attr('class', 'title')
      .attr('x', width/2  - 20)
      .attr('y', -20)
      .attr('text-anchor', 'middle')
      .style("font-size", "100%")
      .style("text-decoration", "underline") 
      .text("IBM Watson Sentement Analysis Results (GoodReads)")
 
// Add the X Axis
svg.append("g")
   .attr("class", "x axis")
   .attr("transform", `translate(0,${height - margin.top - margin.bottom})`)
   .call(xAxis);

// Add the Y Axis
svg.append("g")
   .attr("class", "y axis")
   .call(yAxis); 