let PATH = "C:\\YOUR\\SCRIPT\\PATH\\output.json";

let createStack = (type, name, lore, stack_size, damage, glint, additional_nbt = null) => {
    let item = new Item(type);
    item.setStackSize(stack_size);
    item = item.getItemStack();

    let tag = new net.minecraft.nbt.NBTTagCompound();
    if (additional_nbt !== null) tag = net.minecraft.nbt.JsonToNBT.func_180713_a(additional_nbt);

    let new_nbt = new net.minecraft.nbt.NBTTagList();
    lore.forEach((line) => {
        if (line.length > 0) {
            new_nbt.func_74742_a(new net.minecraft.nbt.NBTTagString(line));
        } else {
            new_nbt.func_74742_a(new net.minecraft.nbt.NBTTagString("§0"));
        }
    });

    tag.func_74782_a("display", new net.minecraft.nbt.NBTTagCompound());
    tag.func_74775_l("display").func_74778_a("Name", name);
    tag.func_74775_l("display").func_74782_a("Lore", new_nbt);

    if (glint) {
        tag.func_74782_a("ench", new net.minecraft.nbt.NBTTagList());
    }

    item.func_77964_b(damage);
    item.func_77982_d(tag);
    item = new Item(item);
    
    return item;
}

let addItem = (slot, stack) => {
	Client.sendPacket(new net.minecraft.network.play.client.C10PacketCreativeInventoryAction(slot, stack));
}

let data = JSON.parse(FileLib.read(PATH));

new Thread(() => {
    Thread.sleep(3000);

    Object.values(data).forEach(frame => {
        frame.push("\ndebuggings.dev"); // free advertisement. You can remove this line if you want.
        let item = createStack("stone", "§fStone", frame, 1, 0, false);
        addItem(36, item.getItemStack());

        Thread.sleep(100);
    });
}).start();
