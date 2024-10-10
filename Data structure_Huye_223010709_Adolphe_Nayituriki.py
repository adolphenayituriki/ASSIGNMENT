class ParcelsDeliveryService:
      print("PARCELS DELIVERY SERVICES ")
      print("_________________________________ \n")
      def __init__(self):
            self.parcels = []
            self.delivery_queue = []
            self.undo_stack = []
      def add_parcels(self, parcel):
            parcel = str(input("Enter parcels you want to add: "))
            self.parcels.append(parcel)                                                        # Push
            self.delivery_queue.append(parcel)                                           # Push
            print(f"The {parcel} parcel,  added to be delivered")
      def processing_parcels(self):
            if self.delivery_queue:
                  parcel = self.delivery_queue
                  parcel = str(input("Enter parcel you want to be delivered: "))
                  print(f"The '{parcel}' was delivered ")
                  self.undo_stack.append(parcel)                                           # Push
                  self.parcels.remove(parcel)
            else: print("no parcel to be delivered ")
      def undo_parcels(self):
            if self.undo_stack:
                  parcel = str(input("Enter any parcels you want to undo"))
                  self.undo_stack.pop()                                                          # Pop
                  self.delivery_queue.append(parcel)                                    # Push
                  self.parcels.append(parcel)
                  print(f"Undid is '{parcel}' ")
            else: print('no parcel to undo')
      def list_parcels(self):
            if self.parcels:
                  print(f"-CURRENT PARCELS, ARE: ", ' , '.join(self.parcels))
            else: 
                  print("no current parcels remaining")
            # example,
if __name__ ==  "__main__":
      services = ParcelsDeliveryService()
      
      services.add_parcels(" ")
      services.add_parcels(" ")
      services.add_parcels(" ")
      services.add_parcels(" ")
      services.list_parcels()
      
      services.processing_parcels()
      services.processing_parcels()
      services.list_parcels()
      
      services.undo_parcels()
      services.undo_parcels()
      services.list_parcels()
