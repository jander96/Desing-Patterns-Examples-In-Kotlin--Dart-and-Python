main() {
  final device = TV();

  final basicControl = TvBasicControl(device);
  print(
      "TV State -> isTurnOn: ${device.isEnable} Volume: ${device.vol}, Channel: ${device.chan}");
  basicControl.tooglePower();
  basicControl.volumeUp();
  basicControl.channelUp();
  print(
      "TV State -> isTurnOn: ${device.isEnable} Volume: ${device.vol}, Channel: ${device.chan}");
}

abstract class Device {
  bool isEnable = false;
  int chan = 0;
  int vol = 0;

  void enable();
  void disable();
  int getVolume();
  void setVolume(int percent);
  int getChannel();
  void setChannel(int number);
}

abstract class RemoteControl {
  void tooglePower();
  void volumeDown();
  void volumeUp();
  void channelDown();
  void channelUp();
}

class TV extends Device {
  void enable() {
    print("Power on");
    isEnable = true;
  }

  void disable() {
    print("Power off");
    isEnable = false;
  }

  int getVolume() {
    print("Getting volume");
    return vol;
  }

  void setVolume(int percent) {
    vol = getVolume() + percent;
  }

  int getChannel() {
    print("Getting channel ");
    return chan;
  }

  void setChannel(int number) {
    chan = getChannel() + number;
  }
}

class TvBasicControl extends RemoteControl {
  final Device device;
  TvBasicControl(this.device);

  void tooglePower() {
    device.isEnable ? device.disable() : device.enable();
  }

  void volumeDown() {
    device.setVolume(-10);
  }

  void volumeUp() {
    device.setVolume(10);
  }

  void channelDown() {
    device.setChannel(-1);
  }

  void channelUp() {
    device.setChannel(1);
  }
}

class TvModernControl extends RemoteControl {
  final Device device;
  TvModernControl(this.device);

  void tooglePower() {
    device.isEnable ? device.disable() : device.enable();
  }

  void volumeDown() {
    device.setVolume(-10);
  }

  void volumeUp() {
    device.setVolume(10);
  }

  void channelDown() {
    device.setChannel(-1);
  }

  void channelUp() {
    device.setChannel(1);
  }

  // Others advance functions
  void mute() {
    device.setVolume(0);
  }
}
