import React from 'react';
import { Dropdown } from 'semantic-ui-react';

const CustomDropdown = (props) => {

    return (
        <Dropdown
            fluid
            selection
            search={props.searchable}
            options={props.options}
            value={props.selectedValue}
            onChange={props.changed}>
        </Dropdown>
    );
}

export default CustomDropdown;