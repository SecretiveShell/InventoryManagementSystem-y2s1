C4Context
title Books4Bucks - System Context Diagram

Person(admin, "Admin", "Admin users who manage the system.")
Person(clerk, "Clerk", "Clerk users who interact with the system to manage book transactions.")

System(books4Bucks, "Books4Bucks", "A system for managing book inventories, sales, and user activities.")

Rel_D(admin, books4Bucks, "Manages system configurations and user permissions", "HTTP/HTTPS")
Rel_D(clerk, books4Bucks, "Handles book transactions, updates inventory, and assists customers", "HTTP/HTTPS")

Boundary(System_Boundary, "Books4Bucks") {
    System(books4Bucks, "Books4Bucks", "A system for managing book inventories, sales, and user activities.")
}
Boundary(System_Boundry, "Printer"){
System_Ext(Printer, "Printer", "An external printer used for printing receipts and reports")
}
Rel_D(books4Bucks, Printer, "Sends print data", "USB/Wireless")

UpdateRelStyle(admin,books4Bucks , $offsetY="-30", $offsetX="-150")
UpdateRelStyle(clerk,books4Bucks , $offsetY="-50", $offsetX="-150")
UpdateRelStyle(books4Bucks, Printer, $offsetY="-40", $offsetX="-40")
