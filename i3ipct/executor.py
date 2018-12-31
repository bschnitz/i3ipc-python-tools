import i3ipc
from .find import Finder

class Executor():
  def __init__(self, prefix):
    self.count = 0
    self.prefix = prefix
    self.callback = lambda i3, window: None
    self.callbacks = {}

  def onNewWindow(self, on_new_window):
    self.callback = on_new_window
    return self

  def onDone(self, on_done):
    self.on_done = on_done
    return self

  def exec(self, cmd):
    self.i3 = i3ipc.Connection()
    workspace = self.i3.get_tree().find_focused().workspace().name

    ident = '{prefix}_{count}'.format(prefix=self.prefix, count=self.count)
    self.callbacks[ident] = self.callback
    self.count += 1
    self.i3.command('workspace '+ident)
    self.i3.command('exec '+cmd)
    self.i3.on('window::new', lambda i3, e: self.on_new_window(i3, e))

    self.i3.command('workspace '+workspace)
    return self

  def loop(self):
    self.i3.main()
    return self

  def on_new_window(self, i3, e):
    windows = Finder(i3.get_tree()).find(id=e.container.id)
    window = windows[0] if windows else None
    callback = self.callbacks.pop(window.workspace().name, None)
    if callback != None:
      callback(self, i3, window)
    if not self.callbacks:
      self.on_done(self, i3)
