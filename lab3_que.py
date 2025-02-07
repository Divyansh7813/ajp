import matplotlib.pyplot as plt

segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]


plt.figure(figsize=(4, 4))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%', startangle=120, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Revenue Distribution Across Business Segments')
plt.axis('equal') 
plt.show()