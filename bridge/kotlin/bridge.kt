

 fun main() {
    val device = TV()

    val basicControl = TvBasicControl(device)
    println("TV State -> isTurnOn: ${device.isEnable} Volume: ${device.vol}, Channel: ${device.chan}")
    basicControl.tooglePower()
    basicControl.volumeUp()
    basicControl.channelUp()
    println("TV State -> isTurnOn: ${device.isEnable} Volume: ${device.vol}, Channel: ${device.chan}")

}

interface Device {

    var isEnable: Boolean
    var chan: Int
    var vol: Int

    fun enable()
    fun disable()
    fun getVolume(): Int
    fun setVolume(percent: Int)
    fun getChannel(): Int
    fun setChannel(number: Int)
}

interface RemoteControl {

    fun tooglePower()
    fun volumeDown()
    fun volumeUp()
    fun channelDown()
    fun channelUp()
}

class TV() : Device {

    override var isEnable: Boolean = false

    override var chan: Int = 0

    override var vol: Int = 0

    override fun enable() {
        println("Power on")
        isEnable = true
    }

    override fun disable() {
        println("Power off")
        isEnable = false
    }

    override fun getVolume(): Int {
        println("Getting volume")
        return vol
    }

    override fun setVolume(percent: Int) {
        vol = getVolume() + percent
    }

    override fun getChannel(): Int {
        println("Getting channel ")
        return chan
    }

    override fun setChannel(number: Int) {
        chan = getChannel() + number
    }
}

class TvBasicControl(private val device: Device) : RemoteControl {

    override fun tooglePower() {
        if (device.isEnable) {
            device.disable()
        } else {
            device.enable()
        }
    }

    override fun volumeDown() {
        device.setVolume(-10)
    }

    override fun volumeUp() {
        device.setVolume(10)
    }

    override fun channelDown() {
        device.setChannel(-1)
    }

    override fun channelUp() {
        device.setChannel(1)
    }
}


class TvModernControl(private val device: Device) : RemoteControl {

    override fun tooglePower() {
        if (device.isEnable) {
            device.disable()
        } else {
            device.enable()
        }
    }

    override fun volumeDown() {
        device.setVolume(-10)
    }

    override fun volumeUp() {
        device.setVolume(10)
    }

    override fun channelDown() {
        device.setChannel(-1)
    }

    override fun channelUp() {
        device.setChannel(1)
    }

    // Others advance functions
    fun mute(){
        device.setVolume(0)
    }
}