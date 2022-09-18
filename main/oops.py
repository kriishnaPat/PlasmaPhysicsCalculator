	@@ -1,26 +1,39 @@
1	- class Length:
1	+ #parent class
2	-     in_unit = 0
3	-     out_unit = 0
4	-     in_value = 0
5	-     def set_values(self, in_unit, out_unit, in_value):
6	-         Length.in_u = in_unit
7	-         Length.out_u = out_unit
8	-         Length.in_value = in_value 
9	-
102	  class Polygon:
113	      width = 0
124	      length = 0
135	      radius = 0
146	      def set_values(self, width, length, radius):
157	          Polygon.width = width
168	          Polygon.length = length
179	          Polygon.radius = radius
18	-
10	+         
11	+ #inharenting classes       
12	+ class rectangle(Polygon):
13	+     def area(self):
14	+         return self.width * self.length
15	+     
16	+     
17	+ class triangle(Polygon):
18	+     def area(self):
19	+         return self.width * self.length / 2
20	+     
21	+     
1922	  class circle(Polygon):
2023	      def area(self):
2124	          return 3.14159265358979323846 * self.radius * 2
2225	        
26	+
27	+ class Length:
28	+     in_unit = 0
29	+     out_unit = 0
30	+     in_value = 0
31	+     def set_values(self, in_unit, out_unit, in_value):
32	+         Length.in_u = in_unit
33	+         Length.out_u = out_unit
34	+         Length.in_value = in_value 
35	+         
2336	  # inharenting classes for each conversion
2437	  # these show what the value is going to be converted in to 
2538	  # ex) out_mm turns cm -> mm
2639	  class out_mm(Length):
@@ -119,410 +132,94 @@
119132	      def inch(self):
120133	          return self.in_value / 63360
121134	      def foot(self):
122135	          return self.in_value / 5280
123	-  
124	- print()
125	- print()
126	- print("Avalible Units:")
127	- print("----------------")
128	- print()
129	- print("mm")
130	- print()
131	- print("cm")
132	- print()
133	- print("m")
134	- print()
135	- print("km")
136	- print()
137	- print("inch")
138	- print()
139	- print("foot")
140	- print()
141	- print("mile")
142	- print()
143	- print()
144	-     
145136	 
146	- # while loop to continue propting the program 
147	- go = True
148137	 
149	- while go: 
150	-     
151	-   
138	+ rect = rectangle()
139	+ tri = triangle()
140	+ cir = circle()
152	- # can choose the units/ in value
153	-   out_unit = input("What unit would you like to calculate?: ") 
154	-   print() 
155	-   in_unit = input("what unit are you currentley using: ")
156	-   print()
157	-   in_value = float(input("what value do you have: "))
158	-   x = 0
159	-   
160141	 
161	- # setes the input functions to spacific values  
142	+ go = True
162	-   out_mm.set_values(x, in_unit, out_unit, in_value)
163	-   out_cm.set_values(x, in_unit, out_unit, in_value)
164	-   out_m.set_values(x, in_unit, out_unit, in_value)
165143	 
144	+ while go:
145	+     # can choose the units/ in value
146	+     in_shape = input("What shape would you like to calculate?: ")
166147	 
167	- # dictionary of formulas/ pulls dict keys 
168	-   formulas_dict = {"mm-cm": out_cm().mm(),
169	-                   "m-cm":         out_cm().m(),
170	-                   "km-cm":        out_cm().km(),
171	-                   "inch-cm":      out_cm().inch(),
172	-                   "foot-cm":      out_cm().foot(),
173	-                   "mile-cm":      out_cm().mile(),
174	-                   "cm-mm":        out_mm().cm(),
175	-                   "m-mm":         out_mm().m(),
176	-                   "km-mm":        out_mm().km(),
177	-                   "inch-mm":      out_mm().inch(),
178	-                   "foot-mm":      out_mm().foot(),
179	-                   "mile-mm":      out_mm().mile(),
180	-                   "mm-km":        out_km().mm(),
181	-                   "cm-km":        out_km().cm(),
182	-                   "m-km":         out_km().m(),
183	-                   "inch-km":      out_km().inch(),
184	-                   "foot-km":      out_km().foot(),
185	-                   "mile-km":      out_km().mile(),
186	-                   "inch-mm":      out_mm().inch(),
187	-                   "foot-mm":      out_mm().foot(),
188	-                   "mile-mm":      out_mm().mile(),
189	-                   "mm-inch":      out_inch().mm(),
190	-                   "cm-inch":      out_inch().cm(),
191	-                   "m-inch":       out_inch().m(),
192	-                   "km-inch":      out_inch().km(),
193	-                   "foot-inch":    out_inch().foot(),
194	-                   "mile-inch":    out_inch().mile(),
195	-                   "mm-foot":      out_foot().mm(),
196	-                   "cm-foot":      out_foot().cm(),
197	-                   "m-foot":       out_foot().m(),
198	-                   "km-foot":      out_foot().km(),
199	-                   "inch-foot":    out_foot().inch(),
200	-                   "mile-foot":    out_foot().mile(),
201	-                   "mm-mile":      out_mile().mm(),
202	-                   "cm-mile":      out_mile().cm(),
203	-                   "m-mile":       out_mile().m(),
204	-                   "km-mile":      out_mile().km(),
205	-                   "foot-mile":    out_mile().foot(),
206	-                   "inch-mile":    out_mile().inch(),}
207	-
208	-   # uses and gates to decide what formula to pull from dictionary
209	-   if out_unit.upper() == "MM": 
210	-       if in_unit.upper() =='CM':
211	-             print("The conversion from cm to mm is:")
212	-             print(formulas_dict["cm-mm"])
213	-
214	-       elif in_unit.upper() =='M':
215	-             print("The conversion from m to mm is:")
216	-             print(formulas_dict['m-mm'])
217	-
218	-       elif in_unit.upper() =='KM':
219	-             print("The conversion from km to mm is:")
220	-             print(formulas_dict['km-mm'])
221	-
222	-       elif in_unit.upper() =='INCH':
223	-             print("conversion from inches to mm is:")
224	-             print(formulas_dict['inch-mm'])
225	-
226	-       elif in_unit.upper() =='FOOT':
227	-             print("The conversion from feet to mm is:")
228	-             print(formulas_dict['foot-mm'])
229	-       
230	-       elif in_unit.upper() =='MILE':
231	-             print("The conversion from miles to mm is:")
232	-             print(formulas_dict['mile-mm'])
233	-           
234	-       else:
235	-             print()
236	-             print("Error, unit not found in dict")
237	-
238	-   elif out_unit.upper() == "CM":
239	-
240	-       if in_unit.upper() =='MM':
241	-             print("The conversion from mm to cm is:")
242	-             print(formulas_dict['cm-mm'])
243	-
244	-       elif in_unit.upper() =='M':
245	-               print("The conversion from m to cm is:")
246	-               print(formulas_dict['m-mm'])
247	-
248	-       elif in_unit.upper() =='KM':
249	-               print("The conversion from km to cm is:")
250	-               print(formulas_dict['km-mm'])
251	-
252	-       elif in_unit.upper() =='INCH':
253	-               print("conversion from inches to cm is:")
254	-               print(formulas_dict['inch-mm'])
255	-
256	-       elif in_unit.upper() =='FOOT':
257	-             print("The conversion from feet to cm is:")
258	-             print(formulas_dict['foot-mm'])
259	-         
260	-       elif in_unit.upper() =='MILE':
261	-             print("The conversion from miles to cm is:")
262	-             print(formulas_dict['mile-mm'])
263	-             
264	-       else:
265	-             print()
266	-             print("Error, unit not found in dict")
267	-
268	-   elif out_unit.upper() == "M":
269	-
270	-       if in_unit.upper() =='MM':
271	-             print("The conversion from mm to m is:")
272	-             print(formulas_dict['cm-m'])
273	-
274	-       elif in_unit.upper() =='CM':
275	-               print("The conversion from cm to m is:")
276	-               print(formulas_dict['m-m'])
277	-
278	-       elif in_unit.upper() =='KM':
279	-               print("The conversion from km to m is:")
280	-               print(formulas_dict['km-m'])
281	-
282	-       elif in_unit.upper() =='INCH':
283	-               print("conversion from inches to m is:")
284	-               print(formulas_dict['inch-m'])
285	-
286	-       elif in_unit.upper() =='FOOT':
287	-             print("The conversion from feet to m is:")
288	-             print(formulas_dict['foot-m'])
289	-         
290	-       elif in_unit.upper() =='MILE':
291	-             print("The conversion from miles to m is:")
292	-             print(formulas_dict['mile-m'])
293	-             
294	-       else:
295	-             print()
296	-             print("Error, unit not found in dict")
297	-
298	-   elif out_unit.upper() == "KM":
299	-
300	-       if in_unit.upper() =='MM':
301	-             print("The conversion from mm to km is:")
302	-             print(formulas_dict['cm-km'])
303	-
304	-       elif in_unit.upper() =='CM':
305	-               print("The conversion from cm to km is:")
306	-               print(formulas_dict['m-km'])
307	-
308	-       elif in_unit.upper() =='M':
309	-               print("The conversion from m to km is:")
310	-               print(formulas_dict['km-km'])
311	-
312	-       elif in_unit.upper() =='INCH':
313	-               print("conversion from inches to km is:")
314	-               print(formulas_dict['inch-km'])
315	-
316	-       elif in_unit.upper() =='FOOT':
317	-             print("The conversion from feet to km is:")
318	-             print(formulas_dict['foot-km'])
319	-         
320	-       elif in_unit.upper() =='MILE':
321	-             print("The conversion from miles to km is:")
322	-             print(formulas_dict['mile-km'])
323	-             
324	-       else:
325	-             print()
326	-             print("Error, unit not found in dict")
327	-
328	-   elif out_unit.upper() == "INCH":
329	-
330	-       if in_unit.upper() =='MM':
331	-             print("The conversion from mm to inches is:")
332	-             print(formulas_dict['mm-inch'])
333	-
334	-       elif in_unit.upper() =='CM':
335	-               print("The conversion from cm to inches is:")
336	-               print(formulas_dict['cm-inch'])
337	-
338	-       elif in_unit.upper() =='M':
339	-               print("The conversion from m to inches is:")
340	-               print(formulas_dict['m-inch'])
341	-
342	-       elif in_unit.upper() =='KM':
343	-               print("conversion from inches to inches is:")
344	-               print(formulas_dict['km-inch'])
345	-
346	-       elif in_unit.upper() =='FOOT':
347	-             print("The conversion from feet to inches is:")
348	-             print(formulas_dict['foot-inch'])
349	-         
350	-       elif in_unit.upper() =='MILE':
351	-             print("The conversion from miles to inches is:")
352	-             print(formulas_dict['mile-inch'])
353	-             
354	-       else:
355	-             print()
356	-             print("Error, unit not found in dict")
357	-           
358	-   elif out_unit.upper() == "FOOT":
359	-
360	-       if in_unit.upper() =='MM':
361	-             print("The conversion from mm to feet is:")
362	-             print(formulas_dict['mm-foot'])
363	-
364	-       elif in_unit.upper() =='CM':
365	-               print("The conversion from cm to feet is:")
366	-               print(formulas_dict['cm-foot'])
367	-
368	-       elif in_unit.upper() =='M':
369	-               print("The conversion from m to feet is:")
370	-               print(formulas_dict['m-foot'])
371	-
372	-       elif in_unit.upper() =='KM':
373	-               print("conversion from km to feet is:")
374	-               print(formulas_dict['km-foot'])
375	-
376	-       elif in_unit.upper() =='INCH':
377	-             print("The conversion from inches to feet is:")
378	-             print(formulas_dict['inch-foot'])
379	-         
380	-       elif in_unit.upper() =='MILE':
381	-             print("The conversion from miles to feet is:")
382	-             print(formulas_dict['mile-foot'])
383	-             
384	-       else:
385	-             print()
386	-             print("Error, unit not found in dict")
387	-
388	-   elif out_unit.upper() == "MILE":
389	-
390	-       if in_unit.upper() =='MM':
391	-             print("The conversion from mm to miles is:")
392	-             print(formulas_dict['mile-mm'])
393	-
394	-       elif in_unit.upper() =='CM':
395	-               print("The conversion from cm to miles is:")
396	-               print(formulas_dict['cm-mile'])
397	-
398	-       elif in_unit.upper() =='M':
399	-               print("The conversion from m to miles is:")
400	-               print(formulas_dict['m-mile'])
401	-
402	-       elif in_unit.upper() =='KM':
403	-               print("conversion from km to miles is:")
404	-               print(formulas_dict['km-mile'])
405	-
406	-       elif in_unit.upper() =='INCH':
407	-             print("The conversion from inch to miles is:")
408	-             print(formulas_dict['inch-mile'])
409	-         
410	-       elif in_unit.upper() =='FOOT':
411	-             print("The conversion from feet to miles is:")
412	-             print(formulas_dict['foot-mile'])
413	-             
414	-       else:
415	-             print()
416	-             print("Error, unit not found in dict")
417	-
418	-
419	- #POLYGON CODE
420	-     rect = rectangle()
421	-     tri = triangle()
422	-     cir = circle()
423	-  
424	-     
425	- # list of the shapes 
426	-     print()
427	-     print()
428	-     print("Avalible Shapes:")
429	-     print("----------------")
430	-     print()
431	-     print("Hexigon")
432	-     print()
433	-     print("Circle")
434	-     print()
435	-     print("Rectangle")
436	-     print()
437	-     print("Triangle")
438	-     print()
439	-     print("Trapizoide")
440	-     print()
441	-     print()
442	-
443	-
444	- # can choose the shapes/ decides what inputs are applicable 
445	-     in_shape = input("What shape would you like to calculate?: ")
446	-     
447148	      if in_shape.upper() == ("CIRCLE"):
448	-         Z = float(input("enter the redius of the object- without units: "))
149	+         Z = float(input("enter the redius of the object"))
150	+         U = input("enter the units of the value: ")
449151	      elif in_shape.upper() == ("HEXIGON"):
450152	          Y = float(input("enter the length of the object- without units: "))
451153	          X = float(input("enter the width of the object- without units: "))
452154	          Z = 0
155	+         U = input("enter the units of the value: ")
453156	      elif in_shape.upper() == ("RECTANGLE"):
454157	          Y = float(input("enter the length of the object- without units: "))
455158	          X = float(input("enter the width of the object- without units: "))
456159	          Z = 0
160	+         U = input("enter the units of the value: ")
457161	      elif in_shape.upper() == ("TRIANGLE"):
458162	          Y = float(input("enter the length of the object- without units: "))
459163	          X = float(input("enter the width of the object- without units: "))
460164	          Z = 0
165	+         U = input("enter the units of the value: ")
461166	      elif in_shape.upper() == ("TRAPIZOIDE"):
462167	          Y = float(input("enter the length of the object- without units: "))
463168	          X = float(input("enter the width of the object- without units: "))
464169	          Z = 0
170	+         U = input("enter the units of the value: ")
465171	      else:
466172	          print("Please enter a valid shape from the list")
467173	     
468174	 
469175	      rect.set_values(X, Y, Z)
470176	      tri.set_values(X, Y, Z)
471177	      cir.set_values(X, Y, Z)
472178	 
473	-
474	- # dictionary of formulas/ pulls dict keys 
475	-     formulas_dict = {"h6": rect.area() + tri.area() * 2,
476	-                "c0": cir.area(),
477	-                "r4": rect.area(),
478	-                "t3": tri.area(),
479	-                "t4":(rect.area() + tri.area() * 2) / 2}
480	-
481	-
482	-     if in_shape.upper() == "HEXIGON":
483	-         print("The area of your hexigon is:")
484	-         print(formulas_dict['h6'])
485	-
486	-     elif in_shape.upper() == "CIRCLE":
487	-         print("The area of your circle is:")
488	-         print(formulas_dict['c0'])
489	-
490	-     elif in_shape.upper() == "RECTANGLE":
491	-         print("The area of your rectangle is:")
492	-         print(formulas_dict['r4'])
493	-
494	-     elif in_shape.upper() == "TRIANGLE":
495	-         print("The area of your triangle is:")
496	-         print(formulas_dict['t3'])
497	-
498	-     elif in_shape.upper() == "TRAPIZOIDE":
499	-         print("The area of your trapizoide is:")
500	-         print(formulas_dict['t4'])
501	-
502	-     else:
503	-         print()
504	-         print("Error, shape not in dict- fix")
505	-         
506	- # Continue or stop the program
507	-    
508	-
509	-
510	-
511	-   # Continue or stop the program by setting the True while loop to False 
512	-     print()
513	-     going = input("Continue? (Y)es or (N)o: ")
514	-     print()
515	-     print()
516	-     print()
517	-         
518	-     if going.upper() == 'Y':
519	-             go = True
179	+     if U.upper() != "CM":
180	+       cm_convt = {"mm-cm": out_cm().mm(),
181	+                  "m-cm":  out_cm().m(),
182	+                  "km-cm":        out_cm().km(),
183	+                  "inch-cm":      out_cm().inch(),
184	+                  "foot-cm":      out_cm().foot(),
185	+                  "mile-cm":      out_cm().mile(),}
186	+     
187	+   formulas_dict = {"mm-cm": out_cm().mm(),
188	+                  "m-cm":         out_cm().m(),
189	+                    "km-cm":        out_cm().km(),
190	+                    "inch-cm":      out_cm().inch(),
191	+ 172    -                   "foot-cm":      out_cm().foot(),
192	+ 173    -                   "mile-cm":      out_cm().mile(),
193	+ 174    -                   "cm-mm":        out_mm().cm(),
194	+ 175    -                   "m-mm":         out_mm().m(),
195	+ 176    -                   "km-mm":        out_mm().km(),
196	+ 177    -                   "inch-mm":      out_mm().inch(),
197	+ 178    -                   "foot-mm":      out_mm().foot(),
198	+ 179    -                   "mile-mm":      out_mm().mile(),
199	+ 180    -                   "mm-km":        out_km().mm(),
200	+                    "cm-km":        out_km().cm(),
201	+                    "m-km":         out_km().m(),
202	+                   "inch-km":      out_km().inch(),
203	+                    "foot-km":      out_km().foot(),
204	+                    "mile-km":      out_km().mile(),
205	+ 186    -                   "inch-mm":      out_mm().inch(),
206	+ 187    -                   "foot-mm":      out_mm().foot(),
207	+ 188    -                   "mile-mm":      out_mm().mile(),
208	+ 189    -                   "mm-inch":      out_inch().mm(),
209	+ 190    -                   "cm-inch":      out_inch().cm(),
210	+ 191    -                   "m-inch":       out_inch().m(),
211	+ 192    -                   "km-inch":      out_inch().km(),
212	+ 193    -                   "foot-inch":    out_inch().foot(),
213	+ 194    -                   "mile-inch":    out_inch().mile(),
214	+ 195    -                   "mm-foot":      out_foot().mm(),
215	+ 196    -                   "cm-foot":      out_foot().cm(),
216	+ 197    -                   "m-foot":       out_foot().m(),
217	+ 198    -                   "km-foot":      out_foot().km(),
218	+ 199    -                   "inch-foot":    out_foot().inch(),
219	+ 200    -                   "mile-foot":    out_foot().mile(),
220	+ 201    -                   "mm-mile":      out_mile().mm(),
221	+ 202    -                   "cm-mile":      out_mile().cm(),
222	+ 203    -                   "m-mile":       out_mile().m(),
223	+ 204    -                   "km-mile":      out_mile().km(),
224	+ 205    -                   "foot-mile":    out_mile().foot(),
225	+ 206    -                   "inch-mile":    out_mile().inch(),}
520	-     elif going.upper() == 'N':
521	-             go = False
522	-     else:
523	-             print("Enter 'Y' for yes or 'N' for no")