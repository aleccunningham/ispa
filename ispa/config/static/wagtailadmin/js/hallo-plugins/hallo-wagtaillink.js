// Generated by CoffeeScript 1.6.2
(function() {
    (function($) {
        return $.widget('IKS.hallowagtaillink', {
            options: {
                uuid: '',
                editable: null
            },
            populateToolbar: function(toolbar) {
                var buttonSet, addButton, cancelButton, getEnclosingLink, widget;

                widget = this;
                getEnclosingLink = function() {
                    var node;

                    node = widget.options.editable.getSelection().commonAncestorContainer;
                    return $(node).parents('a').get(0);
                };

                buttonSet = $('<span class="' + this.widgetName + '"></span>');

                addButton = $('<span></span>');
                addButton = addButton.hallobutton({
                    uuid: widget.options.uuid,
                    editable: widget.options.editable,
                    label: 'Add/Edit Link',
                    icon: 'icon-link',
                    command: null,
                    queryState: function(event) {
                        return addButton.hallobutton('checked', !!getEnclosingLink());
                    }
                });
                addButton.on('click', function() {
                    var enclosingLink, lastSelection, url, urlParams, href, pageId, linkType;

                    // Defaults.
                    url = window.chooserUrls.pageChooser;
                    urlParams = {
                        'allow_external_link': true,
                        'allow_email_link': true
                    };

                    enclosingLink = getEnclosingLink();
                    lastSelection = widget.options.editable.getSelection();

                    if (enclosingLink) {
                        href = enclosingLink.getAttribute('href');
                        parentPageId = enclosingLink.getAttribute('data-parent-id');
                        linkType = enclosingLink.getAttribute('data-linktype');

                        urlParams['link_text'] = enclosingLink.innerText;

                        if (linkType == 'page' && parentPageId) {
                            url = window.chooserUrls.pageChooser + parentPageId.toString() + '/';
                        } else if (href.startsWith('mailto:')) {
                            url = window.chooserUrls.emailLinkChooser;
                            href = href.replace('mailto:', '');
                            urlParams['link_url'] = href;
                        } else if (!linkType) {  /* external link */
                            url = window.chooserUrls.externalLinkChooser;
                            urlParams['link_url'] = href;
                        }
                    } else if (!lastSelection.collapsed) {
                        urlParams['link_text'] = lastSelection.toString();
                    }

                    return ModalWorkflow({
                        url: url,
                        urlParams: urlParams,
                        responses: {
                            pageChosen: function(pageData) {
                                var a, text, linkHasExistingContent;

                                if (enclosingLink) {
                                    // Editing an existing link
                                    a = enclosingLink;
                                    linkHasExistingContent = true;
                                } else if (!lastSelection.collapsed) {
                                    // Turning a selection into a link

                                    a = document.createElement('a');
                                    lastSelection.surroundContents(a);

                                    // unlink all previously existing links in the selection,
                                    // now nested within 'a'
                                    $('a[href]', a).each(function() {
                                        var parent = this.parentNode;
                                        while (this.firstChild) parent.insertBefore(this.firstChild, this);
                                        parent.removeChild(this);
                                    });

                                    linkHasExistingContent = true;
                                } else {
                                    // Inserting a new link at the cursor position
                                    a = document.createElement('a');
                                    lastSelection.insertNode(a);
                                    linkHasExistingContent = false;
                                }

                                // Set link attributes
                                a.setAttribute('href', pageData.url);
                                if (pageData.id) {
                                    a.setAttribute('data-id', pageData.id);
                                    a.setAttribute('data-parent-id', pageData.parentId);
                                    a.setAttribute('data-linktype', 'page');
                                } else {
                                    a.removeAttribute('data-id');
                                    a.removeAttribute('data-parent-id');
                                    a.removeAttribute('data-linktype');
                                }

                                if (pageData['prefer_this_title_as_link_text'] || !linkHasExistingContent) {
                                    // overwrite existing link content with the returned 'title' text
                                    a.innerText = pageData.title;
                                }

                                return widget.options.editable.element.trigger('change');
                            }
                        }
                    });
                });
                buttonSet.append(addButton);

                cancelButton = $('<span></span>');
                cancelButton = cancelButton.hallobutton({
                    uuid: widget.options.uuid,
                    editable: widget.options.editable,
                    label: 'Remove Link',
                    icon: 'icon-chain-broken',
                    command: null,
                    queryState: function(event) {
                        if (!!getEnclosingLink()) {
                            return cancelButton.hallobutton('enable');
                        } else {
                            return cancelButton.hallobutton('disable');
                        }
                    }
                });
                cancelButton.on('click', function() {
                    var enclosingLink, sel, range;

                    enclosingLink = getEnclosingLink();
                    if (enclosingLink) {
                        sel = rangy.getSelection();
                        range = sel.getRangeAt(0);

                        range.setStartBefore(sel.anchorNode.parentNode);
                        range.setEndAfter(sel.anchorNode.parentNode);

                        sel.setSingleRange(range, false);

                        document.execCommand('unlink');
                        widget.options.editable.element.trigger('change');
                    }
                });
                buttonSet.append(cancelButton);

                buttonSet.hallobuttonset();
                toolbar.append(buttonSet);
            }
        });
    })(jQuery);

}).call(this);
