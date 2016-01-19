herbs ={
'Achillea millefolium': 'Yarrow',
'Acorus calamus': 'Calamus', 
'Aletris farinosa':'Unicorn root',
'Allium sativum':'Garlic',
'Allium cepa':'Onion',
'Aloe Barbadensis':'Aloe',
'Anemone pulsatilla':'Pasque flower',
'Areca catechu':'Betel Nut tree',
'Arnica montana': 'Arnica',
'Artemesia absinthinum': 'Wormwood',
'Ascelepias tuberosa':'Butterfly weed',
'Berberis vulgaris': 'Berberry',
'Brassica': 'Mustard',
'Brayera anthelmintica':'Kosso',
'Caffea arabica': 'Coffee',
'Capsicum frutescens':'Tabassco Chili pepper',
'Caulophyllum thalictroides':'Blue Cohosh',
'Cephalis ipecacuanha':'Syrup ipecac',
'Chelidonium majus':'Sallowwort',
'Chenopodium ambrosoides':'Jesuits tea',
'Cimicifuga racemosa': 'Black Cohosh',
'Cinchona ledgeriana': 'Quinine',
'Cinnamomum camphora': 'Cinnamon',
'Cinnamomum zeylanicum': '',
'Citrullus colocynthis':'',
'Claviceps purpurea':'',
'Colchicum autumnale':'',
'Conium maculatum':'',
'Crocus sativa':'',
'Croton tiglium':'',
'Cytisus scoparius':'',
'Drypoteris filixmas':'',
'Ephedra vulgaris':'ma huang',
'Erythroxylon coca':'',
'Foeniculum vulgare':'Fennel',
'Gelsemium sempervirens':'',
'Glycyrrhiza glabra':'licorice',
'Hedeoma pulegioides':'',
'Helleborus niger':'',
'Hydrastis canadensis':'Goldenseal',
'Juniperus communis':'juniper',
'Lavandula officinalis':'Lavender',
'Lobaria pulmonaria': 'Lungwort'}

def hang_herbs(herbs):
	latin = herbs.keys()
	print(latin)


def main():
	print(herbs)
	print("$$$$$$$$$$$$$$")
	print(herbs['Lobaria pulmonaria'])
	hang_herbs(herbs)

main()