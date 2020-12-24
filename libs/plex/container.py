# MediaContainer = Framework.objects.MediaContainer
# Container = Framework.modelling.objects.Container
# Object = Framework.modelling.objects.Object

# noinspection PyPep8Naming,PyUnresolvedReferences
class ObjectContainer(list):
    """
    <MediaContainer object> from logging
    """
    view_group = "Stub"
    art = "Stub"
    title1 = "Stub"
    title2 = "Stub"
    noHistory = False  # Stub
    replaceParent = False  # Stub

    def Append(self, result):
        """
        :param result: MetadataSearchResult
        """
        list.append(self, result)


class ObjectMetaclass(type):

    def __eq__(cls, other):
        # Allow comparison of object classes based on their name, since we synthesise different
        # classes for each sandbox that should be considered equivalent.
        #
        return cls != Object and other != Object and hasattr(other, '__mro__') and Object in other.__mro__ and (cls.__name__ == other.__name__)

    def __getattr__(cls, name):
        return cls._class_attributes[name]

    def __setattr__(cls, name, value):
        if name in cls.__dict__ or name[0] == '_':
            super(ObjectMetaclass, cls).__setattr__(cls, name, value)
        else:
            if cls._attribute_list != None and name not in cls._attribute_list:
                raise Framework.exceptions.FrameworkException("Object of type '%s' has no attribute named '%s'" % (str(cls), name))
            cls._class_attributes[name] = value


class Object(object):
    __metaclass__ = ObjectMetaclass
    _attribute_list = list()
    _class_attributes = dict()
    _unique = False

    xml_tag = 'Object'

    def __init__(self, **kwargs):
        self._response_headers = {'Content-Type': 'application/xml'}
        self._attributes = {}
        for name in kwargs:
            setattr(self, name, kwargs[name])

    @property
    def _core(self):
        """
          Easy access to the core
        """
        return type(self)._sandbox._core

    @property
    def _context(self):
        """
          Easy access to the context.
        """
        return type(self)._sandbox.context

    def _set_attribute(self, el, name, value):
        try:
            if isinstance(value, bool):
                value = '1' if value else '0'
            elif isinstance(value, (Framework.components.localization.LocalString, Framework.components.localization.LocalStringPair, Framework.components.runtime.HostedResource, int, long)):
                value = str(value)
            elif isinstance(value, dict):
                value = None
            if value != None:
                el.set(convert_name(name), value)
        except:
            self._core.log_exception("Exception setting attribute '%s' of object %s to %s (type: %s)", name, str(self), str(value), str(type(value)))

    def _to_xml(self, excluded_attrs=[]):
        root = self._core.data.xml.element(type(self).xml_tag)

        for name in type(self)._class_attributes:
            if name not in excluded_attrs:
                self._set_attribute(root, name, type(self)._class_attributes[name])

        for name in self._attributes:
            if name not in excluded_attrs:
                self._set_attribute(root, name, self._attributes[name])

        return root

    def _get_response_status(self):
        return 200

    def _get_response_headers(self):
        return self._response_headers

    @property
    def headers(self):
        return self._response_headers

    def __hasattr__(self, name):
        return name in self._attributes or name in self.__dict__

    def __getattr__(self, name):
        if name[0] != '_':
            if name in self._attributes:
                return self._attributes[name]
            elif name in self._attribute_list:
                return None

        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name[0] != '_':
            if self._attribute_list != None and name not in self._attribute_list:
                raise Framework.exceptions.FrameworkException("Object of type '%s' has no attribute named '%s'" % (str(type(self)), name))
            self._attributes[name] = value
            return
        object.__setattr__(self, name, value)

class Container(Object):
    _children_attr_name = 'objects'
    _child_types = []

    def __init__(self, **kwargs):
        setattr(self, '_objects', [])

        if self._children_attr_name in kwargs:
            for obj in kwargs[self._children_attr_name]:
                self.add(obj)

            del kwargs[self._children_attr_name]

        Object.__init__(self, **kwargs)

    def _to_xml(self, excluded_attrs=[]):
        ea = list(excluded_attrs)
        if type(self)._children_attr_name not in ea:
            ea.append(type(self)._children_attr_name)
        root = Object._to_xml(self, ea)
        self._append_children(root, self._objects)
        return root

    def _append_children(self, root, children):
        if children:
            for obj in children:
                el = obj._to_xml()
                if el != None:
                    root.append(el)

    def add(self, obj):
        for obj_type in type(self)._child_types:
            if isinstance(obj, obj_type):
                cls = type(obj)
                # Check whether the object should be unique within the container.
                if cls._unique:
                    for other in self._objects:
                        if isinstance(other, cls):
                            raise Framework.exceptions.FrameworkException("Only one object of type '%s' can be added to a container." % cls.__name__)

                self._objects.append(obj)
                return

        raise Framework.exceptions.FrameworkException("Object of type '%s' cannot be added to this container." % str(type(obj)))

    def extend(self, obj_list):
        # If passed a container, extract the object list.
        if isinstance(obj_list, Container):
            obj_list = obj_list._objects
        for obj in obj_list:
            self.add(obj)

    def __len__(self):
        return len(self._objects)

    def __nonzero__(self):
        return True

    def __hasattr__(self, name):
        if name == self._children_attr_name:
            return True
        return Object.__hasattr__(self, name)

    def __getattr__(self, name):
        if name == self._children_attr_name:
            return self._objects
        return Object.__getattr__(self, name)

    def __setattr__(self, name, value):
        if name == self._children_attr_name:
            self._objects = value
            return
        Object.__setattr__(self, name, value)


class MediaContainer(XMLContainer):

    def __init__(self, core, art=None, viewGroup=None, title1=None, title2=None, noHistory=False, replaceParent=False, disabledViewModes=None, **kwargs):
        XMLContainer.__init__(self, core, art=art, title1=title1, title2=title2, noHistory=noHistory, replaceParent=replaceParent, **kwargs)

        if viewGroup is not None:
            if viewGroup in self._core.runtime.view_groups:
                self.viewGroup = viewGroup
            else:
                self._core.log.error("(Framework) Couldn't assign view group '%s' to a MediaContainer - group doesn't exist" % viewGroup)
                pass

        if type(disabledViewModes) == list:
            dvString = ""
            for view in disabledViewModes:
                if view in Framework.components.runtime.view_modes:
                    if len(dvString) > 0: dvString += ","
                    dvString += str(Framework.components.runtime.view_modes[view])
            self.disabledViewModes = dvString

    def __valueOrNone(self, key):
        if self.__dict__.has_key(key):
            return str(self.__dict__[key])
        else:
            return None

    def ToElement(self):
        if self.__dict__.has_key("contextMenu"):
            __containerContextMenu = self.contextMenu
            self.contextMenu = None
        else:
            __containerContextMenu = None
        root = XMLObject.ToElement(self)
        for item in self.__items__:
            if item.__dict__.has_key("contextMenu"):
                __itemContextMenu = item.contextMenu
                item.contextMenu = None
            else:
                __itemContextMenu = None

            if item.__dict__.has_key("contextKey"):
                __itemContextKey = item.contextKey
                item.contextKey = None
            else:
                __itemContextKey = None

            if item.__dict__.has_key("contextArgs"):
                __itemContextArgs = item.contextArgs
                item.contextArgs = None
            else:
                __itemContextArgs = None

            if isinstance(item, XMLObject):
                info = ItemInfoRecord()
                info.title1 = self.__valueOrNone("title1")
                info.title2 = self.__valueOrNone("title2")
                info.art = self.__valueOrNone("art")
                if item.__dict__.has_key("title"):
                    info.itemTitle = item.title
                elif item.__dict__.has_key("name"):
                    info.itemTitle = item.name

                if 'art' in item.__dict__ and item.art != None:
                    info.art = str(item.art)

                if 'thumb' in item.__dict__ and item.thumb != None:
                    info.thumb = str(item.thumb)

                # Add sender information to functions
                def add_sender_arg(obj):
                    if isinstance(obj, Function):
                        obj.AddFunctionArguments(sender=info)
                    elif isinstance(obj, list):
                        for x in obj:
                            add_sender_arg(x)
                    if hasattr(obj, '__items__'):
                        add_sender_arg(obj.__items__)
                    if hasattr(obj, '__dict__'):
                        if 'key' in obj.__dict__:
                            add_sender_arg(obj.key)
                        if 'items' in obj.__dict__:
                            add_sender_arg(obj.items)
                        if 'parts' in obj.__dict__:
                            add_sender_arg(obj.parts)

                add_sender_arg(item)

                __itemElement = item.ToElement()

                # Check if there's a context menu
                if __itemContextKey:
                    __contextMenu = None
                    if __itemContextMenu:
                        __contextMenu = __itemContextMenu
                    elif __containerContextMenu:
                        __contextMenu = __containerContextMenu
                    if __contextMenu:
                        __itemElement.append(__contextMenu.ToElement(info, __itemContextKey, **__itemContextArgs))

                root.append(__itemElement)

            item.contextMenu = __itemContextMenu
            item.contextKey = __itemContextKey
            item.contextArgs = __itemContextArgs

        root.set("size", str(len(self)))

        if hasattr(self, "viewGroup"):
            grp = self._core.runtime.view_groups[self.viewGroup]
            if grp.viewMode: root.set("viewmode", str(grp.viewMode))
            if grp.mediaType: root.set("contenttype", str(grp.mediaType))
            if grp.viewType: root.set("viewType", str(grp.viewType))
            if grp.viewMenu != None:
                if grp.viewMenu:
                    root.set("viewMenu", "1")
                else:
                    root.set("viewMenu", "0")
            if grp.viewThumb != None:
                if grp.viewThumb:
                    root.set("viewThumb", "1")
                else:
                    root.set("viewThumb", "0")
            if grp.viewCols != None: root.set("viewCols", str(grp.viewCols))
            if grp.viewRows != None: root.set("viewRows", str(grp.viewRows))
            if grp.viewSummary != None: root.set("viewSummary", str(grp.viewSummary))

        root.set("identifier", str(self._core.identifier))

        self.contextMenu = __containerContextMenu
        return root

    def __getitem__(self, item):

        # If requesting a slice, construct a new container with the specified items
        if isinstance(item, slice):

            # Create a new container
            c = MediaContainer(self._core)

            # Copy all container attributes from old to new
            for key in self.__dict__:
                if key[0] != "_" and self.__dict__[key].__class__.__name__ != "function" and key != "tagName" and self.__dict__[key] != None:
                    value = self.__dict__[key]
                    c.__dict__[key] = value

            # Get the items specified by the slice, add them to the new container and return it
            c.__items__ = XMLContainer.__getitem__(self, item)
            return c

        # Otherwise, return a single item
        else:
            return XMLContainer.__getitem__(self, item)